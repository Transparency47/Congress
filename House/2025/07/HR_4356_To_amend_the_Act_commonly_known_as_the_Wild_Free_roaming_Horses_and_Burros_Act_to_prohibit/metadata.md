# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4356?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4356
- Title: Wild Horse and Burro Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4356
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2026-01-08T09:07:08Z
- Update date including text: 2026-01-08T09:07:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4356",
    "number": "4356",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Wild Horse and Burro Protection Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-08T09:07:08Z",
    "updateDateIncludingText": "2026-01-08T09:07:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-07-10T15:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "TN"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "AZ"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MI"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "PA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "PA"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "MA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "DC"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NC"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NC"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NJ"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CO"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "HI"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "CT"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "IL"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4356ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4356\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Ms. Titus (for herself, Mr. Cohen , and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Act commonly known as the Wild Free-roaming Horses and Burros Act to prohibit certain uses of aircraft with respect to the management of wild free-roaming horses and burros, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wild Horse and Burro Protection Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAs part of efforts to control equine populations under law, the Bureau of Land Management is directed to humanely capture wild free-roaming horses and burros for adoption.\n**(2)**\nThe use of helicopters to chase equines over prolonged distances, usually on rough terrain, is particularly dangerous, and can frighten the animals and lead to deadly situations, often miles from public view.\n**(3)**\nPublic observation of roundups is typically limited, thereby restricting public access to the government operation.\n**(4)**\nScientific research shows that more humane and cost-effective alternatives exist to control equine populations, including fertility controls.\n**(5)**\nSince fiscal year 2012, over $69.5 million in taxpayer dollars have funded roundup operations to remove federally protected wild horses and burros from the range.\n**(6)**\nIn the past five years (2020\u20132024), at least $36.7 million has been spent on roundups, including over $6 million paid to helicopter roundup contractors in fiscal year 2022 alone.\n**(7)**\nSince 2012, the Bureau of Land Management has administered fewer than 800 fertility control treatments per year on average. In fiscal year 2012, 1,045 treatments were applied; in fiscal year 2024, 1,038 treatments.\n**(8)**\nHistorically, the Bureau of Land Management\u2019s Wild Horse and Burro Program has spent less than one percent of its budget on implementing fertility controls.\n**(9)**\nThe elimination of helicopters from the Bureau of Land Management\u2019s gatherings would provide a more humane method of capturing equines, and provide significant savings to taxpayers.\n#### 3. Amendments to the Wild Free-roaming Horses and Burros Act\nSection 9 of the Act commonly known as the Wild Free-roaming Horses and Burros Act ( Public Law 92\u2013195 ; 16 U.S.C. 1338a ) is amended\u2014\n**(1)**\nby striking In administering this Act and inserting (a) In general .\u2014In administering this Act ;\n**(2)**\nby striking helicopters or, for the purpose of transporting captured animals, motor vehicles and inserting motor vehicles for the purpose of transporting captured animals or aircraft only in compliance with subsection (b) of this section ;\n**(3)**\nby striking fixed-wing aircraft, or helicopters, or to and inserting or ; and\n**(4)**\nby adding at the end the following:\n(b) Phased elimination of certain uses of aircraft In administering this Act, during the 2-year period after the date of the enactment of the Wild Horse and Burro Protection Act of 2025 , the Secretary shall phase out the use or contracts for the use of helicopters or fixed-wing aircraft for the purposes of rounding up or gathering wild free-roaming horses and burros, ensuring an effective reduction in the reliance on these methods each year until all such practices have been terminated. (c) Requirement for use of cameras on aircraft Any helicopter or aircraft used for the purposes of rounding up or gathering wild horses and burros shall be equipped with one or more cameras to record the roundup or gather operation. The Secretary shall ensure such footage is made available as part of the corresponding agency roundup or gather report. .\n#### 4. GAO Report\nNot later than 1 year after the date of the enactment of this Act, the Comptroller General shall submit, to the Committee on Natural Resources of the House of Representatives and the Committee on Energy and Natural Resources of the Senate, a report that describes\u2014\n**(1)**\nhumane alternatives to the use of helicopters and fixed-wing aircraft in managing wild free-roaming horse and burro populations;\n**(2)**\njob creation opportunities presented by the use of such humane alternatives; and\n**(3)**\nthe effects of aircraft, including unmanned aircraft systems, on wild free-roaming horse and burro populations.",
      "versionDate": "2025-07-10",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Animals",
        "updateDate": "2025-08-01T15:13:48Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4356ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Wild Horse and Burro Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:51Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wild Horse and Burro Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T08:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Act commonly known as the Wild Free-roaming Horses and Burros Act to prohibit certain uses of aircraft with respect to the management of wild free-roaming horses and burros, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T08:05:52Z"
    }
  ]
}
```
