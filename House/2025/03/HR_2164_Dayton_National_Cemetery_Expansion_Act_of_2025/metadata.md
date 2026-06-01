# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2164?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2164
- Title: Dayton National Cemetery Expansion Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2164
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-03-27T08:06:30Z
- Update date including text: 2026-03-27T08:06:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-30 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2026-02-03 - Committee: Subcommittee Hearings Held
- 2026-03-26 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-03-26 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-30 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2026-02-03 - Committee: Subcommittee Hearings Held
- 2026-03-26 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-03-26 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2164",
    "number": "2164",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000463",
        "district": "10",
        "firstName": "Michael",
        "fullName": "Rep. Turner, Michael R. [R-OH-10]",
        "lastName": "Turner",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Dayton National Cemetery Expansion Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:30Z",
    "updateDateIncludingText": "2026-03-27T08:06:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-03",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-30",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:07:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-27T03:14:15Z",
                "name": "Reported by"
              },
              {
                "date": "2026-03-26T14:25:26Z",
                "name": "Markup by"
              },
              {
                "date": "2026-02-03T16:51:07Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-01-30T16:40:59Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2164ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2164\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Turner of Ohio introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo authorize the Secretary of Veterans Affairs to enter into an agreement with the Montgomery County Land Bank for the transfer of certain land near Dayton National Cemetery to the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dayton National Cemetery Expansion Act of 2025 .\n#### 2. Authorization of transfer of certain land near Dayton National Cemetery to Department of Veterans Affairs\n##### (a) Transfer\nNot later than 30 days after the date on which the Montgomery County Land Bank makes an offer to transfer to the Department of Veterans Affairs the parcel of land described in subsection (b), the Secretary of Veterans Affairs shall begin the process of entering into an agreement with the Land Bank to carry out such transfer. Under any such agreement\u2014\n**(1)**\nthe Land Bank shall agree to transfer to the Department all right, title, and interest in such parcel at no cost of the land to the Department and for no consideration; and\n**(2)**\nthe Secretary shall agree to accept such transfer\u2014\n**(A)**\nin order to use such parcel as a national cemetery; and\n**(B)**\nnot later than three years after the date on which the Land Bank offers to transfer the parcel.\n##### (b) Parcel described\nThe parcel of land described in this subsection is the approximately 58 acres of land located in Dayton, Ohio, across from Dayton National Cemetery, bound by the intersection of McCall St. and South Gettysburg Avenue, the intersection of McCall Street and Resaca Avenue, the intersection of South Gettysburg Avenue and U.S. Route 35 of the Interstate Highway System, and depicted on the map titled Dayton National Cemetery Proposed Land Transfer and dated January 26, 2024, and labeled on the map as Expansion Area .\n##### (c) Rules of construction\nNothing in this section shall be construed to\u2014\n**(1)**\nrequire or encourage the Secretary to acquire any parcel other than the parcel described in subsection (b); or\n**(2)**\nrequire or encourage the Secretary to enter into any special agreement with an entity other than the Montgomery County Land Bank.\n##### (d) Montgomery County Land Bank defined\nIn this section, the Montgomery County Land Bank means the land bank located at 130 W. Second Street, Suite 1425, Dayton, Ohio 45402.",
      "versionDate": "2025-03-14",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Cemeteries and funerals",
            "updateDate": "2026-03-10T18:49:46Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2026-03-10T18:49:46Z"
          },
          {
            "name": "Ohio",
            "updateDate": "2026-03-10T18:49:46Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2026-03-10T18:49:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-09T15:39:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119hr2164",
          "measure-number": "2164",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-06-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2164v00",
            "update-date": "2025-06-17"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Dayton National Cemetery Expansion Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to begin the process of entering into an agreement with the Montgomery County Land Bank not later than 30 days after the date on which the land bank makes an offer to transfer at no cost a specified parcel of land in Dayton, Ohio, to the VA to expand the Dayton National Cemetery.</p>"
        },
        "title": "Dayton National Cemetery Expansion Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2164.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dayton National Cemetery Expansion Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to begin the process of entering into an agreement with the Montgomery County Land Bank not later than 30 days after the date on which the land bank makes an offer to transfer at no cost a specified parcel of land in Dayton, Ohio, to the VA to expand the Dayton National Cemetery.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hr2164"
    },
    "title": "Dayton National Cemetery Expansion Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dayton National Cemetery Expansion Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to begin the process of entering into an agreement with the Montgomery County Land Bank not later than 30 days after the date on which the land bank makes an offer to transfer at no cost a specified parcel of land in Dayton, Ohio, to the VA to expand the Dayton National Cemetery.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hr2164"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2164ih.xml"
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
      "title": "Dayton National Cemetery Expansion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dayton National Cemetery Expansion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Veterans Affairs to enter into an agreement with the Montgomery County Land Bank for the transfer of certain land near Dayton National Cemetery to the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:33:34Z"
    }
  ]
}
```
