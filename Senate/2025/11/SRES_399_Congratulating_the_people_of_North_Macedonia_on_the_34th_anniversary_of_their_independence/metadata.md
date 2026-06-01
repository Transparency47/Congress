# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/399?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/399
- Title: A resolution congratulating the people of North Macedonia on the 34th anniversary of their independence and celebrating the 30th anniversary of diplomatic relations between North Macedonia and the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 399
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2025-12-02T19:09:30Z
- Update date including text: 2025-12-02T19:09:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Referred to the Committee on Foreign Relations.
- 2025-11-04 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-11-04 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S7905; text: CR 9/17/2025 S6698)
- 2025-11-04 - Discharge: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-11-04 - Committee: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Referred to the Committee on Foreign Relations.
- 2025-11-04 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-11-04 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S7905; text: CR 9/17/2025 S6698)
- 2025-11-04 - Discharge: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-11-04 - Committee: Senate Committee on Foreign Relations discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/399",
    "number": "399",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "A resolution congratulating the people of North Macedonia on the 34th anniversary of their independence and celebrating the 30th anniversary of diplomatic relations between North Macedonia and the United States.",
    "type": "SRES",
    "updateDate": "2025-12-02T19:09:30Z",
    "updateDateIncludingText": "2025-12-02T19:09:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S7905; text: CR 9/17/2025 S6698)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-04",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Foreign Relations discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-11-04",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Foreign Relations discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-11-05T00:25:33Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-09-17T21:18:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "NC"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NH"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres399is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 399\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Mr. Welch (for himself, Mr. Tillis , Mrs. Shaheen , and Mr. Ricketts ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nCongratulating the people of North Macedonia on the 34th anniversary of their independence and celebrating the 30th anniversary of diplomatic relations between North Macedonia and the United States.\nThat the Senate\u2014\n**(1)**\nextends congratulations and best wishes to the people of North Macedonia as they celebrate the 34th anniversary of their independence;\n**(2)**\nhonors the bond of friendship between the United States and North Macedonia and the shared values of freedom, democracy, and good governance;\n**(3)**\nrecognizes the cooperation between the State of Vermont and North Macedonia and the partnership between the Vermont National Guard and the Army of the Republic of North Macedonia;\n**(4)**\nappreciates North Macedonia\u2019s continued commitment to the Prespa Agreement;\n**(5)**\nhonors five years of shared security, collective defense, and joint military alliance with North Macedonia as a member of the North Atlantic Treaty Organization;\n**(6)**\nappreciates North Macedonia\u2019s active role in fostering peace and stability in Eastern Europe and the Western Balkans and advancing democratic reforms and Euro-Atlantic integration, and its alignment with positions of the European Union and the United States on security and foreign policy; and\n**(7)**\nlooks toward many more decades of shared prosperity, peace, cooperation, and friendship.",
      "versionDate": "2025-09-17",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres399ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 399\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Mr. Welch (for himself, Mr. Tillis , Mrs. Shaheen , and Mr. Ricketts ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nNovember 4, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nCongratulating the people of North Macedonia on the 34th anniversary of their independence and celebrating the 30th anniversary of diplomatic relations between North Macedonia and the United States.\nThat the Senate\u2014\n**(1)**\nextends congratulations and best wishes to the people of North Macedonia as they celebrate the 34th anniversary of their independence;\n**(2)**\nhonors the bond of friendship between the United States and North Macedonia and the shared values of freedom, democracy, and good governance;\n**(3)**\nrecognizes the cooperation between the State of Vermont and North Macedonia and the partnership between the Vermont National Guard and the Army of the Republic of North Macedonia;\n**(4)**\nappreciates North Macedonia\u2019s continued commitment to the Prespa Agreement;\n**(5)**\nhonors five years of shared security, collective defense, and joint military alliance with North Macedonia as a member of the North Atlantic Treaty Organization;\n**(6)**\nappreciates North Macedonia\u2019s active role in fostering peace and stability in Eastern Europe and the Western Balkans and advancing democratic reforms and Euro-Atlantic integration, and its alignment with positions of the European Union and the United States on security and foreign policy; and\n**(7)**\nlooks toward many more decades of shared prosperity, peace, cooperation, and friendship.",
      "versionDate": "2025-11-04",
      "versionType": "ATS"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-11-17T15:01:05Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-11-17T15:00:51Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-11-17T15:00:41Z"
          },
          {
            "name": "North Macedonia",
            "updateDate": "2025-11-17T15:00:35Z"
          },
          {
            "name": "Sovereignty, recognition, national governance and status",
            "updateDate": "2025-11-17T15:00:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-09-19T16:32:59Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres399is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres399ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution congratulating the people of North Macedonia on the 34th anniversary of their independence and celebrating the 30th anniversary of diplomatic relations between North Macedonia and the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T02:48:14Z"
    },
    {
      "title": "A resolution congratulating the people of North Macedonia on the 34th anniversary of their independence and celebrating the 30th anniversary of diplomatic relations between North Macedonia and the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T10:56:18Z"
    }
  ]
}
```
