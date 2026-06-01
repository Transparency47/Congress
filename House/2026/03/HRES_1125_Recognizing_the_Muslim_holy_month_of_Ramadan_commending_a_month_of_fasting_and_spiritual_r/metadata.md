# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1125?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1125
- Title: Recognizing the Muslim holy month of Ramadan, commending a month of fasting and spiritual renewal, and extending best wishes to Muslims in the United States and across the globe for a joyous and meaningful observance of Eid al-Fitr.
- Congress: 119
- Bill type: HRES
- Bill number: 1125
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-04-21T00:22:09Z
- Update date including text: 2026-04-21T00:22:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-19 - IntroReferral: Submitted in House
- 2026-03-19 - IntroReferral: Submitted in House
- Latest action: 2026-03-19: Submitted in House

## Actions

- 2026-03-19 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-19 - IntroReferral: Submitted in House
- 2026-03-19 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1125",
    "number": "1125",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "D000624",
        "district": "6",
        "firstName": "Debbie",
        "fullName": "Rep. Dingell, Debbie [D-MI-6]",
        "lastName": "Dingell",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Recognizing the Muslim holy month of Ramadan, commending a month of fasting and spiritual renewal, and extending best wishes to Muslims in the United States and across the globe for a joyous and meaningful observance of Eid al-Fitr.",
    "type": "HRES",
    "updateDate": "2026-04-21T00:22:09Z",
    "updateDateIncludingText": "2026-04-21T00:22:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-03-19T13:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MI"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "IN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "DC"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MD"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "IL"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MN"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "NJ"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CA"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1125ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1125\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mrs. Dingell (for herself, Ms. Tlaib , Mr. Carson , Ms. Norton , Mrs. McClain Delaney , Mr. Krishnamoorthi , Ms. Omar , Mr. Pallone , Ms. Simon , Ms. Pressley , and Mr. Subramanyam ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nRecognizing the Muslim holy month of Ramadan, commending a month of fasting and spiritual renewal, and extending best wishes to Muslims in the United States and across the globe for a joyous and meaningful observance of Eid al-Fitr.\nThat the House of Representatives\u2014\n**(1)**\ndemonstrates solidarity with and support for members of the community of Islam in the United States and throughout the world;\n**(2)**\nrecognizes the importance of the Islamic faith;\n**(3)**\nobserves, out of respect for Ramadan tradition, the Muslim holy month of fasting and spiritual renewal; and\n**(4)**\noffers its best wishes to all Muslims celebrating Eid al-Fitr, the conclusion of Ramadan, while also expressing its deepest respect to Muslims in the United States and worldwide on this important occasion.",
      "versionDate": "2026-03-19",
      "versionType": "IH"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-27",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "263",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Recognizing the Muslim holy month of Ramadan, commending a month of fasting and spiritual renewal, and extending best wishes to Muslims in the United States and across the globe for a joyous and meaningful observance of Eid al-Fitr.",
      "type": "HRES"
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-20T23:34:14Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1125ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Recognizing the Muslim holy month of Ramadan, commending a month of fasting and spiritual renewal, and extending best wishes to Muslims in the United States and across the globe for a joyous and meaningful observance of Eid al-Fitr.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T03:33:23Z"
    },
    {
      "title": "Recognizing the Muslim holy month of Ramadan, commending a month of fasting and spiritual renewal, and extending best wishes to Muslims in the United States and across the globe for a joyous and meaningful observance of Eid al-Fitr.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T08:06:57Z"
    }
  ]
}
```
