# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/947?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/947
- Title: Expressing that compelled political litmus tests used by public institutions to require individuals to identify with specific ideological views are directly at odds with the principles of academic freedom and free speech and in violation of the First Amendment of the Constitution.
- Congress: 119
- Bill type: HRES
- Bill number: 947
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-04-06T21:14:30Z
- Update date including text: 2026-04-06T21:14:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-12-11 - IntroReferral: Submitted in House
- 2025-12-11 - IntroReferral: Submitted in House
- Latest action: 2025-12-11: Submitted in House

## Actions

- 2025-12-11 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-12-11 - IntroReferral: Submitted in House
- 2025-12-11 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/947",
    "number": "947",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001210",
        "district": "3",
        "firstName": "Gregory",
        "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
        "lastName": "Murphy",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Expressing that compelled political litmus tests used by public institutions to require individuals to identify with specific ideological views are directly at odds with the principles of academic freedom and free speech and in violation of the First Amendment of the Constitution.",
    "type": "HRES",
    "updateDate": "2026-04-06T21:14:30Z",
    "updateDateIncludingText": "2026-04-06T21:14:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres947ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 947\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Murphy submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing that compelled political litmus tests used by public institutions to require individuals to identify with specific ideological views are directly at odds with the principles of academic freedom and free speech and in violation of the First Amendment of the Constitution.\nThat the House of Representatives\u2014\n**(1)**\ncondemns public institutions of higher education for conditioning admission to any student applicant, or the hiring, reappointment, or promotion of any faculty member, on the applicant or faculty member pledging allegiance to or making a statement of personal support for or opposition to any political ideology or movement, including a pledge or statement regarding diversity, equity, and inclusion, or related topics; and\n**(2)**\ndiscourages any institution from requesting or requiring any such pledge or statement from an applicant or faculty member, as such actions are antithetical to the freedom of speech protected by the First Amendment.",
      "versionDate": "2025-12-11",
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
        "name": "Education",
        "updateDate": "2025-12-15T16:38:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-11",
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
          "measure-id": "id119hres947",
          "measure-number": "947",
          "measure-type": "hres",
          "orig-publish-date": "2025-12-11",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres947v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-12-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution condemns public institutions of higher education (IHEs) for conditioning an individual's admission to or employment at the IHE on the individual pledging allegiance to or making a statement of personal support for or opposition to any political ideology or movement (e.g., diversity, equity, and inclusion). It also discourages IHEs from requesting or requiring any such pledge or statement.</p>"
        },
        "title": "Expressing that compelled political litmus tests used by public institutions to require individuals to identify with specific ideological views are directly at odds with the principles of academic freedom and free speech and in violation of the First Amendment of the Constitution."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres947.xml",
    "summary": {
      "actionDate": "2025-12-11",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution condemns public institutions of higher education (IHEs) for conditioning an individual's admission to or employment at the IHE on the individual pledging allegiance to or making a statement of personal support for or opposition to any political ideology or movement (e.g., diversity, equity, and inclusion). It also discourages IHEs from requesting or requiring any such pledge or statement.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres947"
    },
    "title": "Expressing that compelled political litmus tests used by public institutions to require individuals to identify with specific ideological views are directly at odds with the principles of academic freedom and free speech and in violation of the First Amendment of the Constitution."
  },
  "summaries": [
    {
      "actionDate": "2025-12-11",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution condemns public institutions of higher education (IHEs) for conditioning an individual's admission to or employment at the IHE on the individual pledging allegiance to or making a statement of personal support for or opposition to any political ideology or movement (e.g., diversity, equity, and inclusion). It also discourages IHEs from requesting or requiring any such pledge or statement.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres947"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres947ih.xml"
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
      "title": "Expressing that compelled political litmus tests used by public institutions to require individuals to identify with specific ideological views are directly at odds with the principles of academic freedom and free speech and in violation of the First Amendment of the Constitution.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-12T17:24:36Z"
    },
    {
      "title": "Expressing that compelled political litmus tests used by public institutions to require individuals to identify with specific ideological views are directly at odds with the principles of academic freedom and free speech and in violation of the First Amendment of the Constitution.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-12T09:07:23Z"
    }
  ]
}
```
