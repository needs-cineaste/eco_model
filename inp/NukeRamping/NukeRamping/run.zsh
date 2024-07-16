for rup in $(seq 0.001 0.001 0.200); do
  python model.py $rup
done
