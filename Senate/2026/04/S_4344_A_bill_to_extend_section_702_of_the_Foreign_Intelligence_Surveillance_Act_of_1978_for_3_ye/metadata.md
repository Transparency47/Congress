# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4344?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4344
- Title: A bill to extend section 702 of the Foreign Intelligence Surveillance Act of 1978 for 3 years.
- Congress: 119
- Bill type: S
- Bill number: 4344
- Origin chamber: Senate
- Introduced date: 2026-04-17
- Update date: 2026-05-14T18:51:07Z
- Update date including text: 2026-05-14T18:51:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-17: Introduced in Senate
- 2026-04-17 - IntroReferral: Introduced in Senate
- 2026-04-17 - Calendars: Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time.
- 2026-04-20 - Calendars: Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 373.
- 2026-04-23 - Floor: Cloture motion on the motion to proceed to the measure presented in Senate. (CR S2249)
- 2026-04-23 - Floor: Motion to proceed to consideration of measure made in Senate.
- 2026-05-13 - Floor: Cloture motion on the motion to proceed withdrawn by unanimous consent in Senate. (CR S2249)
- Latest action: 2026-04-17: Introduced in Senate

## Actions

- 2026-04-17 - IntroReferral: Introduced in Senate
- 2026-04-17 - Calendars: Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time.
- 2026-04-20 - Calendars: Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 373.
- 2026-04-23 - Floor: Cloture motion on the motion to proceed to the measure presented in Senate. (CR S2249)
- 2026-04-23 - Floor: Motion to proceed to consideration of measure made in Senate.
- 2026-05-13 - Floor: Cloture motion on the motion to proceed withdrawn by unanimous consent in Senate. (CR S2249)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-17",
    "latestAction": {
      "actionDate": "2026-04-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4344",
    "number": "4344",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "A bill to extend section 702 of the Foreign Intelligence Surveillance Act of 1978 for 3 years.",
    "type": "S",
    "updateDate": "2026-05-14T18:51:07Z",
    "updateDateIncludingText": "2026-05-14T18:51:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Cloture motion on the motion to proceed withdrawn by unanimous consent in Senate. (CR S2249)",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Cloture motion on the motion to proceed to the measure presented in Senate. (CR S2249)",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Motion to proceed to consideration of measure made in Senate.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 373.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-04-17",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time.",
      "type": "Calendars"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-17",
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

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": {
        "actions": {
          "actions": {
            "item": [
              {
                "actionCode": "Intro-S",
                "actionDate": "2026-04-28",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "91000",
                "actionDate": "2026-04-28",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              }
            ]
          },
          "count": "2"
        },
        "amendedBill": {
          "congress": "119",
          "number": "4344",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "A bill to extend section 702 of the Foreign Intelligence Surveillance Act of 1978 for 3 years.",
          "type": "S",
          "updateDateIncludingText": "2026-05-14"
        },
        "chamber": "Senate",
        "congress": "119",
        "number": "5436",
        "sponsors": {
          "item": {
            "bioguideId": "W000790",
            "firstName": "Raphael",
            "fullName": "Sen. Warnock, Raphael G. [D-GA]",
            "lastName": "Warnock",
            "party": "D",
            "state": "GA"
          }
        },
        "submittedDate": "2026-04-28T04:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2026-04-29T11:08:24Z"
      }
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2026-04-17",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4344pcs.xml",
      "text": "II\nCalendar No. 373\n119th CONGRESS\n2d Session\nS. 4344\nIN THE SENATE OF THE UNITED STATES\nApril 17 (legislative day, April 14), 2026 Mr. Cotton (for himself and Mr. Grassley ) introduced the following bill; which was read the first time\nApril 20, 2026 Read the second time and placed on the calendar\nA BILL\nTo extend section 702 of the Foreign Intelligence Surveillance Act of 1978 for 3 years.\n#### 1. Extension of section 702 authority for 3 years\n##### (a) Effective dates\nSection 403(b) of the FISA Amendments Act of 2008 ( Public Law 110\u2013261 ; 122 Stat. 2474) is amended\u2014\n**(1)**\nin paragraph (1) ( 50 U.S.C. 1881 note), by striking two years after the date of enactment of the Reforming Intelligence and Securing America Act and inserting April 20, 2029 ; and\n**(2)**\nin paragraph (2) ( 18 U.S.C. 2511 note), in the matter preceding subparagraph (A), by striking two years after the date of enactment of the Reforming Intelligence and Securing America Act and inserting April 20, 2029 .\n##### (b) Conforming amendment\nSection 404(b)(1) of the FISA Amendments Act of 2008 ( Public Law 110\u2013261 ; 122 Stat. 2476), is amended, in the heading, by striking two years after the date of enactment of the Reforming Intelligence and Securing America Act and inserting April 20, 2029 .",
      "versionDate": "2026-04-20",
      "versionType": "Placed on Calendar Senate"
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
        "actionDate": "2026-04-16",
        "text": "Read twice and referred to the Select Committee on Intelligence."
      },
      "number": "4342",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A bill to extend section 702 of the Foreign Intelligence Surveillance Act of 1978 for 18 months.",
      "type": "S"
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
        "item": {
          "name": "Intelligence activities, surveillance, classified information",
          "updateDate": "2026-04-24T16:44:05Z"
        }
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-23T18:58:50Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4344pcs.xml"
        }
      ],
      "type": "Placed on Calendar Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A bill to extend section 702 of the Foreign Intelligence Surveillance Act of 1978 for 3 years.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-18T10:56:21Z"
    },
    {
      "title": "A bill to extend section 702 of the Foreign Intelligence Surveillance Act of 1978 for 3 years.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-18T10:56:21Z"
    }
  ]
}
```
