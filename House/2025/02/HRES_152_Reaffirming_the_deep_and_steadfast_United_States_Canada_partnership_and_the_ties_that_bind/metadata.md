# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/152?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/152
- Title: Reaffirming the deep and steadfast United States-Canada partnership and the ties that bind the two countries in support of economic and national security.
- Congress: 119
- Bill type: HRES
- Bill number: 152
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2025-05-06T15:09:14Z
- Update date including text: 2025-05-06T15:09:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-02-24 - Committee: Submitted in House
- Latest action: 2025-02-24: Submitted in House

## Actions

- 2025-02-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-02-24 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/152",
    "number": "152",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "A000369",
        "district": "2",
        "firstName": "Mark",
        "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
        "lastName": "Amodei",
        "party": "R",
        "state": "NV"
      }
    ],
    "title": "Reaffirming the deep and steadfast United States-Canada partnership and the ties that bind the two countries in support of economic and national security.",
    "type": "HRES",
    "updateDate": "2025-05-06T15:09:14Z",
    "updateDateIncludingText": "2025-05-06T15:09:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
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
      "actionCode": "H12100",
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-24T17:00:20Z",
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
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "GA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NC"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NV"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NV"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres152ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 152\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Mr. Amodei of Nevada (for himself, Mrs. Fletcher , Mr. Carter of Georgia , Mr. Veasey , Mr. Langworthy , Ms. Ross , Ms. Lee of Nevada , Ms. Titus , and Mr. Costa ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nReaffirming the deep and steadfast United States-Canada partnership and the ties that bind the two countries in support of economic and national security.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes that now, more than ever, the relationship between the United States and Canada is an essential strategic asset to the United States and Americans, and is critical to promoting peace, expanding global economic opportunity, and being prepared to respond to unforeseen events;\n**(2)**\nreaffirms its full commitment to maintain and grow the critical United States-Canada partnership;\n**(3)**\nrecognizes that the security of one country is dependent on the security of the other, and welcomes greater collaboration in the areas of defense, cyber and technology security, and Arctic security;\n**(4)**\nreaffirms its commitment to the bilateral and international alliance between the two countries, which allows both countries to face common threats together and uphold common values, including democracy, human rights, and the rule of law;\n**(5)**\nrecognizes the strategic importance of one of the most secure borders in the world, the comanagement of which facilitates trade and serves as a trusted corridor for their supply chains;\n**(6)**\nrecognizes that bolstering the supply chains of both countries will make both countries more competitive and more resilient in the face of economic aggression from hostile countries;\n**(7)**\nsupports an increased focus on energy security through greater cross-border energy infrastructure, including for oil, natural gas, nuclear energy, renewable energy, and resilient electricity transmission, and through diversifying critical minerals supply chains; and\n**(8)**\nis fully committed to the creation of more well-paying United States jobs through continued trade and investment with Canada.",
      "versionDate": "2025-02-24",
      "versionType": "IH"
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
        "name": "International Affairs",
        "updateDate": "2025-05-06T15:09:14Z"
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
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres152ih.xml"
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
      "title": "Reaffirming the deep and steadfast United States-Canada partnership and the ties that bind the two countries in support of economic and national security.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T09:33:42Z"
    },
    {
      "title": "Reaffirming the deep and steadfast United States-Canada partnership and the ties that bind the two countries in support of economic and national security.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T09:06:08Z"
    }
  ]
}
```
