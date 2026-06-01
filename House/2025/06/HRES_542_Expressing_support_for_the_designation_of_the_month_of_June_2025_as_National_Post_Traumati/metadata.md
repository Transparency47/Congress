# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/542?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/542
- Title: Expressing support for the designation of the month of June 2025 as "National Post-Traumatic Stress Awareness Month" and June 27, 2025, as "National Post-Traumatic Stress Awareness Day".
- Congress: 119
- Bill type: HRES
- Bill number: 542
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2026-03-30T19:37:09Z
- Update date including text: 2026-03-30T19:37:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - IntroReferral: Submitted in House
- 2025-06-24 - IntroReferral: Submitted in House
- Latest action: 2025-06-24: Submitted in House

## Actions

- 2025-06-24 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - IntroReferral: Submitted in House
- 2025-06-24 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/542",
    "number": "542",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000608",
        "district": "50",
        "firstName": "Scott",
        "fullName": "Rep. Peters, Scott H. [D-CA-50]",
        "lastName": "Peters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for the designation of the month of June 2025 as \"National Post-Traumatic Stress Awareness Month\" and June 27, 2025, as \"National Post-Traumatic Stress Awareness Day\".",
    "type": "HRES",
    "updateDate": "2026-03-30T19:37:09Z",
    "updateDateIncludingText": "2026-03-30T19:37:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T14:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-24T14:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "MI"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "FL"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "NJ"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres542ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 542\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Mr. Peters (for himself, Mr. Bergman , Mr. Mast , Mr. Thompson of California , and Mr. Moulton ) submitted the following resolution; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nExpressing support for the designation of the month of June 2025 as National Post-Traumatic Stress Awareness Month and June 27, 2025, as National Post-Traumatic Stress Awareness Day .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National Post-Traumatic Stress Awareness Month and National Post-Traumatic Stress Awareness Day ;\n**(2)**\nsupports the efforts of the Secretary of Veterans Affairs and the Secretary of Defense, as well as the entire medical community, to educate members of the Armed Forces, veterans, the families of members of the Armed Forces and veterans, and the public about the causes, symptoms, and treatment of post-traumatic stress;\n**(3)**\nsupports efforts by the Secretary of Veterans Affairs and the Secretary of Defense to foster cultural change around the issue of post-traumatic stress, understanding that personal interactions can save lives and advance treatment;\n**(4)**\nencourages the leadership of the Armed Forces to support appropriate treatment of men and women of the Armed Forces who suffer from post- traumatic stress; and\n**(5)**\nrecognizes the impact of post-traumatic stress on the spouses and families of members of the Armed Forces and veterans.",
      "versionDate": "2025-06-24",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-08T13:39:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-24",
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
          "measure-id": "id119hres542",
          "measure-number": "542",
          "measure-type": "hres",
          "orig-publish-date": "2025-06-24",
          "originChamber": "HOUSE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres542v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2025-06-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of National Post-Traumatic Stress Awareness Month and National Post-Traumatic Stress Awareness Day.</p><p>The resolution supports (1) the education of members of the Armed Forces, veterans, their families, and the public about post-traumatic stress; and (2) efforts by the Department of Veterans Affairs and the Department of Defense to foster cultural change around the issue of post-traumatic stress.</p><p>The resolution also encourages the leadership of the Armed Forces to support treatment of members of the Armed Forces who suffer from post-traumatic stress.</p>"
        },
        "title": "Expressing support for the designation of the month of June 2025 as \"National Post-Traumatic Stress Awareness Month\" and June 27, 2025, as \"National Post-Traumatic Stress Awareness Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres542.xml",
    "summary": {
      "actionDate": "2025-06-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Post-Traumatic Stress Awareness Month and National Post-Traumatic Stress Awareness Day.</p><p>The resolution supports (1) the education of members of the Armed Forces, veterans, their families, and the public about post-traumatic stress; and (2) efforts by the Department of Veterans Affairs and the Department of Defense to foster cultural change around the issue of post-traumatic stress.</p><p>The resolution also encourages the leadership of the Armed Forces to support treatment of members of the Armed Forces who suffer from post-traumatic stress.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hres542"
    },
    "title": "Expressing support for the designation of the month of June 2025 as \"National Post-Traumatic Stress Awareness Month\" and June 27, 2025, as \"National Post-Traumatic Stress Awareness Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-06-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Post-Traumatic Stress Awareness Month and National Post-Traumatic Stress Awareness Day.</p><p>The resolution supports (1) the education of members of the Armed Forces, veterans, their families, and the public about post-traumatic stress; and (2) efforts by the Department of Veterans Affairs and the Department of Defense to foster cultural change around the issue of post-traumatic stress.</p><p>The resolution also encourages the leadership of the Armed Forces to support treatment of members of the Armed Forces who suffer from post-traumatic stress.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hres542"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres542ih.xml"
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
      "title": "Expressing support for the designation of the month of June 2025 as \"National Post-Traumatic Stress Awareness Month\" and June 27, 2025, as \"National Post-Traumatic Stress Awareness Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T08:18:22Z"
    },
    {
      "title": "Expressing support for the designation of the month of June 2025 as \"National Post-Traumatic Stress Awareness Month\" and June 27, 2025, as \"National Post-Traumatic Stress Awareness Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T08:06:38Z"
    }
  ]
}
```
