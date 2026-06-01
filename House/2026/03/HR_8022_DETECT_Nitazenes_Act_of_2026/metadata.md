# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8022?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8022
- Title: DETECT Nitazenes Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8022
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-05-16T08:07:27Z
- Update date including text: 2026-05-16T08:07:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-03-20 - Committee: Referred to the Subcommittee on Emergency Management and Technology.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-03-20 - Committee: Referred to the Subcommittee on Emergency Management and Technology.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8022",
    "number": "8022",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "DETECT Nitazenes Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:27Z",
    "updateDateIncludingText": "2026-05-16T08:07:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-20",
      "committees": {
        "item": {
          "name": "Emergency Management and Technology Subcommittee",
          "systemCode": "hshm12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Emergency Management and Technology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-20T19:51:24Z",
              "name": "Referred to"
            }
          },
          "name": "Emergency Management and Technology Subcommittee",
          "systemCode": "hshm12"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "VA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8022ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8022\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. Pfluger (for himself, Mr. Vindman , and Mr. Baumgartner ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo require the Science and Technology Directorate in the Department of Homeland Security to work with the Drug Enforcement Agency to develop greater capacity to detect, identify, and disrupt illicit substances, such as nitazenes, in very low concentrations.\n#### 1. Short title\nThis Act may be cited as the Detection Equipment and Technology Evaluation to Counter the Threat of Nitazenes Act of 2026 or the DETECT Nitazenes Act of 2026 .\n#### 2. Enhancing the capacity to detect and identify drugs such as nitazenes\nSection 302(15) of the Homeland Security Act of 2002 ( 6 U.S.C. 182(15) ) is amended, in the matter preceding subparagraph (A), by striking fentanyl and xylazine and inserting fentanyl, xylazine, and nitazenes .",
      "versionDate": "2026-03-19",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-11-03",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3093",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DETECT Nitazenes Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2026-04-06T13:19:44Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8022ih.xml"
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
      "title": "DETECT Nitazenes Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T12:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DETECT Nitazenes Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T12:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Detection Equipment and Technology Evaluation to Counter the Threat of Nitazenes Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T12:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Science and Technology Directorate in the Department of Homeland Security to work with the Drug Enforcement Agency to develop greater capacity to detect, identify, and disrupt illicit substances, such as nitazenes, in very low concentrations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T12:03:27Z"
    }
  ]
}
```
