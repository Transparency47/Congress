# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/107?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/107
- Title: Recognizing the importance of saving lives, reducing gun violence, and strengthening public safety as the United States celebrates its 250th anniversary.
- Congress: 119
- Bill type: HCONRES
- Bill number: 107
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:18:29Z
- Update date including text: 2026-05-30T08:18:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-05-29 - IntroReferral: Submitted in House
- Latest action: 2026-05-29: Submitted in House

## Actions

- 2026-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-05-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-29",
    "latestAction": {
      "actionDate": "2026-05-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/107",
    "number": "107",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001241",
        "district": "47",
        "firstName": "Dave",
        "fullName": "Rep. Min, Dave [D-CA-47]",
        "lastName": "Min",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Recognizing the importance of saving lives, reducing gun violence, and strengthening public safety as the United States celebrates its 250th anniversary.",
    "type": "HCONRES",
    "updateDate": "2026-05-30T08:18:29Z",
    "updateDateIncludingText": "2026-05-30T08:18:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
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
          "date": "2026-05-29T16:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "DC"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "GA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "FL"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "MA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "GA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "WA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "IN"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "MN"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "CT"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "NY"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "IL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "NJ"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "AZ"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "MO"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "FL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres107ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. CON. RES. 107\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2026 Mr. Min (for himself, Ms. Norton , Mr. Johnson of Georgia , Ms. Wilson of Florida , Mr. Lynch , Ms. Williams of Georgia , Mr. Smith of Washington , Mr. Kennedy of New York , Mr. Carson , Ms. Craig , Mr. Carbajal , Mrs. Hayes , Mr. Suozzi , Ms. Chu , Ms. Kelly of Illinois , Mrs. Watson Coleman , Mrs. Grijalva , Mr. Bell , Mr. Frost , Ms. Simon , and Mr. Deluzio ) submitted the following concurrent resolution; which was referred to the Committee on the Judiciary\nCONCURRENT RESOLUTION\nRecognizing the importance of saving lives, reducing gun violence, and strengthening public safety as the United States celebrates its 250th anniversary.\nThat Congress\u2014\n**(1)**\nrecognizes the 250th anniversary of the United States as a moment to reaffirm a national commitment to saving lives, reducing gun violence, and strengthening public safety;\n**(2)**\nhonors the lives lost to gun violence and provides support for survivors, families, and communities impacted;\n**(3)**\ncommends the efforts of community leaders, law enforcement, public health professionals, community violence intervention practitioners, and advocates working to prevent gun violence and promote safety;\n**(4)**\nprioritizes support for law enforcement efforts to collect and publish data about violent crimes, improve clearance rates for homicides and shootings, and expand training in deescalation tactics;\n**(5)**\nsupports expanded investment in proactive, community-based strategies that stop violence before it occurs by identifying individuals at high risk and intervening with credible messengers and customized services that address the root causes of violence;\n**(6)**\ncommits to ensuring robust funding for victim services so many can take the first steps towards recovery;\n**(7)**\naffirms that preventing gun violence and saving lives must be a national priority as the United States enters its next 250 years; and\n**(8)**\npursues policies that strengthen public safety, uphold constitutional rights, and protect the well-being of all people of the United States.",
      "versionDate": "2026-05-29",
      "versionType": "IH"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres107ih.xml"
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
      "title": "Recognizing the importance of saving lives, reducing gun violence, and strengthening public safety as the United States celebrates its 250th anniversary.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:18:29Z"
    },
    {
      "title": "Recognizing the importance of saving lives, reducing gun violence, and strengthening public safety as the United States celebrates its 250th anniversary.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:05:43Z"
    }
  ]
}
```
