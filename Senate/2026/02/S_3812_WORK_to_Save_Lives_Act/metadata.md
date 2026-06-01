# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3812?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3812
- Title: WORK to Save Lives Act
- Congress: 119
- Bill type: S
- Bill number: 3812
- Origin chamber: Senate
- Introduced date: 2026-02-10
- Update date: 2026-04-02T18:27:47Z
- Update date including text: 2026-04-02T18:27:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in Senate
- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2026-02-10: Introduced in Senate

## Actions

- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3812",
    "number": "3812",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "WORK to Save Lives Act",
    "type": "S",
    "updateDate": "2026-04-02T18:27:47Z",
    "updateDateIncludingText": "2026-04-02T18:27:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-10",
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
            "date": "2026-03-19T14:01:16Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-02-10T16:43:32Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "AK"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NM"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "OR"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3812is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3812\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2026 Mr. Merkley (for himself, Ms. Murkowski , Mr. Heinrich , Mr. Schiff , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require the Secretary of Labor to issue guidance and regulations regarding opioid overdose reversal medication and employee training.\n#### 1. Short title\nThis Act may be cited as the Workplace Overdose Reversal Kits to Save Lives Act or the WORK to Save Lives Act .\n#### 2. Non-mandatory guidance for employers concerning opioid overdose reversal medication\n##### (a) In general\nNot later than 270 days after the date of enactment of this Act, the Secretary of Labor, acting through the Occupational Safety and Health Administration, shall issue nonmandatory guidance to employers on\u2014\n**(1)**\nacquiring and maintaining opioid overdose reversal medication; and\n**(2)**\ntraining employees on an annual basis on the usage of such medication.\n##### (b) Employer defined\nIn this section, the term employer has the meaning given such term in section 3 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 652 ), except that such term does not include the United States Postal Service.\n#### 3. Mandatory regulations for Federal agencies concerning opioid overdose reversal medication\n##### (a) In general\nNot later than 270 days after the date of enactment of this Act, the Secretary of Labor, acting through the Occupational Safety and Health Administration, shall issue regulations to require each Federal agency to\u2014\n**(1)**\nacquire and maintain opioid overdose reversal medication; and\n**(2)**\ntrain employees on an annual basis on the usage of such medication.\n##### (b) Federal agency defined\nIn this section, the term Federal agency means any agency or instrumentality of the Federal Government, including the Veterans Health Administration, notwithstanding section 7425(b) of title 38, United States Code.",
      "versionDate": "2026-02-10",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-02-10",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "7479",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "WORK to Save Lives Act",
      "type": "HR"
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
            "name": "Drug therapy",
            "updateDate": "2026-04-02T18:27:25Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2026-04-02T18:27:20Z"
          },
          {
            "name": "Emergency medical services and trauma care",
            "updateDate": "2026-04-02T18:27:41Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2026-04-02T18:27:47Z"
          },
          {
            "name": "Worker safety and health",
            "updateDate": "2026-04-02T18:27:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2026-02-27T16:46:41Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3812is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "WORK to Save Lives Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "WORK to Save Lives Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Workplace Overdose Reversal Kits to Save Lives Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Labor to issue guidance and regulations regarding opioid overdose reversal medication and employee training.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T03:48:24Z"
    }
  ]
}
```
