# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1964?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1964
- Title: Las Cruces Bataan Memorial Clinic Act
- Congress: 119
- Bill type: HR
- Bill number: 1964
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-12-11T09:07:46Z
- Update date including text: 2025-12-11T09:07:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1964",
    "number": "1964",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000136",
        "district": "2",
        "firstName": "Gabe",
        "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
        "lastName": "Vasquez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Las Cruces Bataan Memorial Clinic Act",
    "type": "HR",
    "updateDate": "2025-12-11T09:07:46Z",
    "updateDateIncludingText": "2025-12-11T09:07:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-27T17:59:41Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1964ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1964\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Vasquez introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo name the Department of Veterans Affairs community-based outpatient clinic in Las Cruces, New Mexico, the Las Cruces Bataan Memorial Clinic .\n#### 1. Short title\nThis Act may be cited as the Las Cruces Bataan Memorial Clinic Act .\n#### 2. Name of Department of Veterans Affairs community-based outpatient clinic, Las Cruces, New Mexico\nThe Department of Veterans Affairs community-based outpatient clinic in Las Cruces, New Mexico, shall, after the date of the enactment of this Act, be known and designated as the Las Cruces Bataan Memorial Clinic . Any reference to such clinic in any law, regulation, map, document, record, or other paper of the United States shall be considered to be a reference to the Las Cruces Bataan Memorial Clinic.",
      "versionDate": "2025-03-06",
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
        "actionDate": "2025-03-27",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "1179",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Las Cruces Bataan Memorial Clinic Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-13T15:18:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1964",
          "measure-number": "1964",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2025-07-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1964v00",
            "update-date": "2025-07-01"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Las Cruces Bataan Memorial Clinic Act</strong></p><p>This bill designates the community-based outpatient clinic of the Department of Veterans Affairs in Las Cruces, New Mexico, as the Las Cruces Bataan Memorial Clinic.</p>"
        },
        "title": "Las Cruces Bataan Memorial Clinic Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1964.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Las Cruces Bataan Memorial Clinic Act</strong></p><p>This bill designates the community-based outpatient clinic of the Department of Veterans Affairs in Las Cruces, New Mexico, as the Las Cruces Bataan Memorial Clinic.</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119hr1964"
    },
    "title": "Las Cruces Bataan Memorial Clinic Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Las Cruces Bataan Memorial Clinic Act</strong></p><p>This bill designates the community-based outpatient clinic of the Department of Veterans Affairs in Las Cruces, New Mexico, as the Las Cruces Bataan Memorial Clinic.</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119hr1964"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1964ih.xml"
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
      "title": "Las Cruces Bataan Memorial Clinic Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Las Cruces Bataan Memorial Clinic Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To name the Department of Veterans Affairs community-based outpatient clinic in Las Cruces, New Mexico, the \"Las Cruces Bataan Memorial Clinic\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T05:48:25Z"
    }
  ]
}
```
