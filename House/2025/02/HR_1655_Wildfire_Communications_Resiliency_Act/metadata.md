# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1655?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1655
- Title: Wildfire Communications Resiliency Act
- Congress: 119
- Bill type: HR
- Bill number: 1655
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-06-11T08:05:59Z
- Update date including text: 2025-06-11T08:05:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-03 - Committee: Referred to the Subcommittee on Federal Lands.
- 2025-06-10 - Committee: Subcommittee Hearings Held
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-03 - Committee: Referred to the Subcommittee on Federal Lands.
- 2025-06-10 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1655",
    "number": "1655",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B000668",
        "district": "2",
        "firstName": "Cliff",
        "fullName": "Rep. Bentz, Cliff [R-OR-2]",
        "lastName": "Bentz",
        "party": "R",
        "state": "OR"
      }
    ],
    "title": "Wildfire Communications Resiliency Act",
    "type": "HR",
    "updateDate": "2025-06-11T08:05:59Z",
    "updateDateIncludingText": "2025-06-11T08:05:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
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
      "actionDate": "2025-06-03",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:12:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-06-10T16:59:22Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-06-03T13:58:09Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-27T14:12:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1655ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1655\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Bentz introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide that construction, rebuilding, or hardening of communications facilities following a major disaster or an emergency related to a wildfire is not subject to requirements to prepare certain environmental or historical preservation reviews.\n#### 1. Short title\nThis Act may be cited as the Wildfire Communications Resiliency Act .\n#### 2. Application of NEPA and NHPA to covered communications projects\n##### (a) NEPA exemption\nA Federal authorization with respect to a covered project may not be considered a major Federal action under section 102(2)(C) of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332(2)(C) ).\n##### (b) National Historic Preservation Act exemption\nA covered project may not be considered an undertaking under section 300320 of title 54, United States Code.\n##### (c) Definitions\nIn this section:\n**(1) Chief Executive**\nThe term Chief Executive has the meaning given such term in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ).\n**(2) Communications facility**\nThe term communications facility has the meaning given the term communications facility installation in section 6409(d) of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1455(d) ).\n**(3) Covered project**\nThe term covered project means a project that\u2014\n**(A)**\nis to be carried out entirely within an area for which the President, the Governor of a State, or the Chief Executive of an Indian tribal government has declared a major disaster or an emergency related to a wildfire;\n**(B)**\nis to be carried out not later than 5 years after the date on which the President, Governor, or Chief Executive made such declaration; and\n**(C)**\nreplaces a communications facility damaged by such disaster or emergency or makes improvements to a communications facility in such area that could reasonably be considered as necessary for recovery from such disaster or emergency or to prevent or mitigate any future disaster or emergency.\n**(4) Emergency**\nThe term emergency means\u2014\n**(A)**\nin the case of an emergency declared by the President, an emergency declared by the President under section 501 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5191 ); and\n**(B)**\nin the case of an emergency declared by the Governor of a State or the Chief Executive of an Indian tribal government, any occasion or instance with respect to which the Governor or Chief Executive declares that an emergency exists (or makes a similar declaration) under State or Tribal law (as the case may be).\n**(5) Federal authorization**\nThe term Federal authorization \u2014\n**(A)**\nmeans any authorization required under Federal law with respect to a covered project; and\n**(B)**\nincludes any permits, special use authorizations, certifications, opinions, or other approvals as may be required under Federal law with respect to a covered project.\n**(6) Governor**\nThe term Governor means the chief executive of any State.\n**(7) Indian tribal government**\nThe term Indian tribal government has the meaning given such term in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ).\n**(8) Major disaster**\nThe term major disaster means\u2014\n**(A)**\nin the case of a major disaster declared by the President, a major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ); and\n**(B)**\nin the case of a major disaster declared by the Governor of a State or the Chief Executive of an Indian tribal government, any occasion or instance with respect to which the Governor or Chief Executive declares that a disaster exists (or makes a similar declaration) under State or Tribal law (as the case may be).\n**(9) State**\nThe term State means each State of the United States, the District of Columbia, and each territory or possession of the United States.",
      "versionDate": "2025-02-27",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-21T14:41:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1655",
          "measure-number": "1655",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-05-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1655v00",
            "update-date": "2025-05-15"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Wildfire Communications Resiliency Act</strong></p><p>This bill exempts certain post-wildfire communications infrastructure projects from specified federal environmental and historic preservation review requirements.\u00a0</p><p>Specifically, the bill exempts from review projects that (1) are to be carried out within five years of the declaration of a wildfire-related major disaster or emergency in a given area; (2) are to be carried out entirely within the area for which the major disaster or emergency was declared; and (3) will replace a communications facility damaged by the major disaster or emergency, or make improvements to a communications\u00a0facility that are necessary for recovery or to prevent or mitigate a future major disaster or emergency. To qualify under the bill, a major disaster or emergency must have been declared by the President, a state governor, or a tribal chief executive.\u00a0</p><p>The bill specifies that these projects are not considered <em>major federal actions</em> under the National Environmental Policy Act of 1969 or <em>undertakings</em> under the National Historic Preservation Act, thus exempting such projects from the review procedures required under those acts.</p>"
        },
        "title": "Wildfire Communications Resiliency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1655.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Wildfire Communications Resiliency Act</strong></p><p>This bill exempts certain post-wildfire communications infrastructure projects from specified federal environmental and historic preservation review requirements.\u00a0</p><p>Specifically, the bill exempts from review projects that (1) are to be carried out within five years of the declaration of a wildfire-related major disaster or emergency in a given area; (2) are to be carried out entirely within the area for which the major disaster or emergency was declared; and (3) will replace a communications facility damaged by the major disaster or emergency, or make improvements to a communications\u00a0facility that are necessary for recovery or to prevent or mitigate a future major disaster or emergency. To qualify under the bill, a major disaster or emergency must have been declared by the President, a state governor, or a tribal chief executive.\u00a0</p><p>The bill specifies that these projects are not considered <em>major federal actions</em> under the National Environmental Policy Act of 1969 or <em>undertakings</em> under the National Historic Preservation Act, thus exempting such projects from the review procedures required under those acts.</p>",
      "updateDate": "2025-05-15",
      "versionCode": "id119hr1655"
    },
    "title": "Wildfire Communications Resiliency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Wildfire Communications Resiliency Act</strong></p><p>This bill exempts certain post-wildfire communications infrastructure projects from specified federal environmental and historic preservation review requirements.\u00a0</p><p>Specifically, the bill exempts from review projects that (1) are to be carried out within five years of the declaration of a wildfire-related major disaster or emergency in a given area; (2) are to be carried out entirely within the area for which the major disaster or emergency was declared; and (3) will replace a communications facility damaged by the major disaster or emergency, or make improvements to a communications\u00a0facility that are necessary for recovery or to prevent or mitigate a future major disaster or emergency. To qualify under the bill, a major disaster or emergency must have been declared by the President, a state governor, or a tribal chief executive.\u00a0</p><p>The bill specifies that these projects are not considered <em>major federal actions</em> under the National Environmental Policy Act of 1969 or <em>undertakings</em> under the National Historic Preservation Act, thus exempting such projects from the review procedures required under those acts.</p>",
      "updateDate": "2025-05-15",
      "versionCode": "id119hr1655"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1655ih.xml"
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
      "title": "Wildfire Communications Resiliency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wildfire Communications Resiliency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that construction, rebuilding, or hardening of communications facilities following a major disaster or an emergency related to a wildfire is not subject to requirements to prepare certain environmental or historical preservation reviews.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T09:18:20Z"
    }
  ]
}
```
