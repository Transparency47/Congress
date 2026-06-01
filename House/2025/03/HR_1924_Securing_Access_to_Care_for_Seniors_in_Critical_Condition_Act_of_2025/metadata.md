# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1924?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1924
- Title: Securing Access to Care for Seniors in Critical Condition Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1924
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2026-04-14T08:05:35Z
- Update date including text: 2026-04-14T08:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1924",
    "number": "1924",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001082",
        "district": "1",
        "firstName": "Kevin",
        "fullName": "Rep. Hern, Kevin [R-OK-1]",
        "lastName": "Hern",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Securing Access to Care for Seniors in Critical Condition Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:35Z",
    "updateDateIncludingText": "2026-04-14T08:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
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
          "date": "2025-03-06T14:08:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "WV"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NC"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "OH"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1924ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1924\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Hern of Oklahoma (for himself, Mr. Boyle of Pennsylvania , Mr. Joyce of Pennsylvania , Mrs. Miller of West Virginia , Mr. Smucker , and Ms. Tenney ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to establish a new criterion for the nonapplication of site-neutral payments to long-term care hospitals under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Securing Access to Care for Seniors in Critical Condition Act of 2025 .\n#### 2. Establishing a new criterion for the nonapplication of site-neutral payments to long-term care hospitals under the Medicare program\nSection 1886(m)(6)(A) of the Social Security Act ( 42 U.S.C. 1395ww(m)(6)(A) ) is amended\u2014\n**(1)**\nin clause (ii)(I), by striking or the ventilator criterion under clause (iv) and inserting , the ventilator criterion under clause (iv), or the high acuity criterion described in clause (v) ; and\n**(2)**\nby adding at the end the following new clause:\n(v) High acuity criterion The criterion specified in this clause (in this paragraph referred to as the high acuity criterion ) for a discharge from a long-term care hospital in a fiscal year is that\u2014 (I) the discharge was assigned to a Medicare-Severity-Long-Term-Care-Diagnosis-Related-Group (MS-LTC-DRG) with a relative weight for such fiscal year that was equal to or greater than 0.8; and (II) the discharge occurred on or after October 1, 2026. .",
      "versionDate": "2025-03-06",
      "versionType": "Introduced in House"
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
        "name": "Health",
        "updateDate": "2025-03-23T10:31:43Z"
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
          "measure-id": "id119hr1924",
          "measure-number": "1924",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2026-02-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1924v00",
            "update-date": "2026-02-13"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Securing Access to Care for Seniors in Critical Condition Act of 2025</strong></p><p>This bill exempts discharges from long-term care hospitals (LTCHs) from the Medicare site-neutral payment rate if the discharge meets specified high acuity criteria and occurs on or after October 1, 2026.\u00a0 (The site-neutral rate is the lower of Medicare\u2019s acute care hospital payment rate under the inpatient prospective payment system or 100% of the cost of the stay. LTCH stays that do not qualify for the specialized LTCH payment rate under Medicare are instead paid at the site-neutral rate.)</p>"
        },
        "title": "Securing Access to Care for Seniors in Critical Condition Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1924.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing Access to Care for Seniors in Critical Condition Act of 2025</strong></p><p>This bill exempts discharges from long-term care hospitals (LTCHs) from the Medicare site-neutral payment rate if the discharge meets specified high acuity criteria and occurs on or after October 1, 2026.\u00a0 (The site-neutral rate is the lower of Medicare\u2019s acute care hospital payment rate under the inpatient prospective payment system or 100% of the cost of the stay. LTCH stays that do not qualify for the specialized LTCH payment rate under Medicare are instead paid at the site-neutral rate.)</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr1924"
    },
    "title": "Securing Access to Care for Seniors in Critical Condition Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing Access to Care for Seniors in Critical Condition Act of 2025</strong></p><p>This bill exempts discharges from long-term care hospitals (LTCHs) from the Medicare site-neutral payment rate if the discharge meets specified high acuity criteria and occurs on or after October 1, 2026.\u00a0 (The site-neutral rate is the lower of Medicare\u2019s acute care hospital payment rate under the inpatient prospective payment system or 100% of the cost of the stay. LTCH stays that do not qualify for the specialized LTCH payment rate under Medicare are instead paid at the site-neutral rate.)</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr1924"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1924ih.xml"
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
      "title": "Securing Access to Care for Seniors in Critical Condition Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T10:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Access to Care for Seniors in Critical Condition Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T10:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to establish a new criterion for the nonapplication of site-neutral payments to long-term care hospitals under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T10:48:30Z"
    }
  ]
}
```
