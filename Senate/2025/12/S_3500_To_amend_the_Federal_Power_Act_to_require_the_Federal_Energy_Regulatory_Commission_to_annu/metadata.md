# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3500?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3500
- Title: Hydropower Licensing Transparency Act
- Congress: 119
- Bill type: S
- Bill number: 3500
- Origin chamber: Senate
- Introduced date: 2025-12-16
- Update date: 2026-04-01T19:38:05Z
- Update date including text: 2026-04-01T19:38:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in Senate
- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2025-12-16: Introduced in Senate

## Actions

- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3500",
    "number": "3500",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Hydropower Licensing Transparency Act",
    "type": "S",
    "updateDate": "2026-04-01T19:38:05Z",
    "updateDateIncludingText": "2026-04-01T19:38:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-16",
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
        "item": {
          "date": "2025-12-16T21:07:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:10Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3500is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3500\nIN THE SENATE OF THE UNITED STATES\nDecember 16, 2025 Ms. Cortez Masto (for herself and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Federal Power Act to require the Federal Energy Regulatory Commission to annually submit to Congress a report on the status of ongoing hydropower relicensing applications.\n#### 1. Short title\nThis Act may be cited as the Hydropower Licensing Transparency Act .\n#### 2. Annual licensing status report\nPart I of the Federal Power Act ( 16 U.S.C. 792 et seq. ) is amended by adding at the end the following:\n37. Annual licensing status report (a) In general Not later than 180 days after the date of enactment of this section, and annually thereafter, the Commission shall submit to Congress a report on the status of\u2014 (1) the licensing process for each new license, and for each subsequent license for which sections 14 and 15 have been waived, for which the existing licensee has notified the Commission under section 15(b)(1) at least 3 years prior to submission of the report that the existing licensee intends to file an application for the new license or subsequent license, but the new license or subsequent license has not yet been issued under section 15; and (2) the licensing process for each original license under section 4(e) for which a citizen, association, corporation, State, Indian Tribe, or municipality has notified the Commission, pursuant to applicable regulations, at least 3 years prior to submission of the report that the citizen, association, corporation, State, Indian Tribe, or municipality intends to file an application for the original license, but the original license has not yet been issued under section 4(e). (b) Inclusions Each report submitted under subsection (a) shall include, with respect to the licensing process for each new license and subsequent license described in that subsection and the licensing process for each original license described in that subsection\u2014 (1) the date the notice of intent described in that subsection was provided to the Commission; (2) any docket number assigned with respect to the licensing process; (3) whether any application for the new license, subsequent license, or original license, as applicable, has been filed; (4) information regarding the status of the application, including the date the Commission anticipates the Commission will issue the original license, subsequent license, or new license, as applicable; (5) the date of any upcoming proceeding or other meeting relating to the original license, subsequent license, or new license, as applicable; and (6) a description of any ongoing or completed actions required of the existing licensee, citizen, association, corporation, State, Indian Tribe, municipality, Commission, any fish and wildlife agency referred to in section 15(b)(3), and any other applicable agency. (c) Disaggregation of information by license type The information included in each report submitted under subsection (a) shall be disaggregated by whether the information relates to a new license, or a subsequent license, issued under section 15 or an original license issued under section 4(e). .",
      "versionDate": "2025-12-16",
      "versionType": "Introduced in Senate"
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
            "name": "Alternative and renewable resources",
            "updateDate": "2026-04-01T18:59:58Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-01T18:25:35Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-01T19:38:05Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-04-01T19:37:51Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-04-01T18:04:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-01-12T16:09:34Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3500is.xml"
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
      "title": "Hydropower Licensing Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Hydropower Licensing Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-09T10:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Power Act to require the Federal Energy Regulatory Commission to annually submit to Congress a report on the status of ongoing hydropower relicensing applications.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-09T10:48:24Z"
    }
  ]
}
```
