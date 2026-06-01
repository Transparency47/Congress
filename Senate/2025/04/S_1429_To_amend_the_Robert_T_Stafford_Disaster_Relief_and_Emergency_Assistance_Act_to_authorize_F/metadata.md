# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1429?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1429
- Title: POWER Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1429
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-04-13T11:20:47Z
- Update date including text: 2026-04-13T11:20:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1429",
    "number": "1429",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "POWER Act of 2025",
    "type": "S",
    "updateDate": "2026-04-13T11:20:47Z",
    "updateDateIncludingText": "2026-04-13T11:20:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T17:34:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NH"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CT"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MS"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NJ"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "OK"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "SD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1429is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1429\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Lankford (for himself, Ms. Hassan , Mr. Blumenthal , Mr. Wicker , Mr. Kim , and Mr. Mullin ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to authorize Federal agencies to provide certain essential assistance for hazard mitigation for electric utilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Opportunities to Widen Electrical Resilience Act of 2025 or the POWER Act of 2025 .\n#### 2. Essential assistance\n##### (a) In general\nSection 403 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170b ) is amended by adding at the end the following:\n(e) Electric utilities (1) Hazard mitigation activities An electric utility may carry out cost-effective hazard mitigation activities jointly or otherwise in combination with activities for the restoration of power carried out with assistance provided under this section. (2) Eligibility for additional assistance In any case in which an electric utility facility receives assistance under this section for the emergency restoration of power, the receipt of such assistance shall not render such facility ineligible for any hazard mitigation assistance under section 406 for which such facility is otherwise eligible. .\n##### (b) Applicability\nThe amendment made by subsection (a) shall only apply to amounts appropriated on or after the date of enactment of this Act.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-09-03",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 57 - 3."
      },
      "number": "4669",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FEMA Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-16",
        "text": "Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "164",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "POWER Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Emergency Management",
        "updateDate": "2025-05-27T16:53:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
    "originChamber": "Senate",
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
          "measure-id": "id119s1429",
          "measure-number": "1429",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2026-04-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1429v00",
            "update-date": "2026-04-13"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Promoting Opportunities to Widen Electrical Resilience Act of 2025 or the POWER Act of 2025</strong></p><p>This bill authorizes electric utilities receiving certain emergency assistance for the restoration of power\u00a0to also carry out cost-effective hazard mitigation activities in combination with the power restoration activities. \u00a0</p><p>Additionally, the bill specifies that electric utilities receiving such assistance for a facility may, if otherwise eligible, also receive hazard mitigation assistance for the same facility under the Federal Emergency Management Agency's Public Assistance program.\u00a0</p>"
        },
        "title": "POWER Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1429.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Promoting Opportunities to Widen Electrical Resilience Act of 2025 or the POWER Act of 2025</strong></p><p>This bill authorizes electric utilities receiving certain emergency assistance for the restoration of power\u00a0to also carry out cost-effective hazard mitigation activities in combination with the power restoration activities. \u00a0</p><p>Additionally, the bill specifies that electric utilities receiving such assistance for a facility may, if otherwise eligible, also receive hazard mitigation assistance for the same facility under the Federal Emergency Management Agency's Public Assistance program.\u00a0</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119s1429"
    },
    "title": "POWER Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Promoting Opportunities to Widen Electrical Resilience Act of 2025 or the POWER Act of 2025</strong></p><p>This bill authorizes electric utilities receiving certain emergency assistance for the restoration of power\u00a0to also carry out cost-effective hazard mitigation activities in combination with the power restoration activities. \u00a0</p><p>Additionally, the bill specifies that electric utilities receiving such assistance for a facility may, if otherwise eligible, also receive hazard mitigation assistance for the same facility under the Federal Emergency Management Agency's Public Assistance program.\u00a0</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119s1429"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1429is.xml"
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
      "title": "POWER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-06T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "POWER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Promoting Opportunities to Widen Electrical Resilience Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to authorize Federal agencies to provide certain essential assistance for hazard mitigation for electric utilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:48:30Z"
    }
  ]
}
```
