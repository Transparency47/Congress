# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3085?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3085
- Title: Expanding Regional Airports Act
- Congress: 119
- Bill type: HR
- Bill number: 3085
- Origin chamber: House
- Introduced date: 2025-04-29
- Update date: 2025-07-31T17:01:37Z
- Update date including text: 2025-07-31T17:01:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-29: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-29 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-04-29: Introduced in House

## Actions

- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-29 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3085",
    "number": "3085",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
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
    "title": "Expanding Regional Airports Act",
    "type": "HR",
    "updateDate": "2025-07-31T17:01:37Z",
    "updateDateIncludingText": "2025-07-31T17:01:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-29",
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
          "date": "2025-04-29T14:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-29T20:49:43Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3085ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3085\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Mr. Vasquez (for himself and Mr. Mann ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to establish a program to provide assistance to underserved airports to improve passenger and flight capacity, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expanding Regional Airports Act .\n#### 2. Regional airport expansion program\n##### (a) In general\nChapter 417 of title 49, United States Code, is amended by adding at the end the following:\nIV Regional Airport Expansion Program 41781. Grants for growing regional airports (a) In general The Secretary of Transportation shall establish a program to provide grants to eligible airports to improve passenger and flight capacity. (b) Eligible uses An eligible airport may use a grant provided under this section for\u2014 (1) activities that improve passenger and flight capacity at such airport, including\u2014 (A) the expansion of passenger and property screening facilities; (B) runway lengthening; (C) construction of hangars and associated infrastructure; and (D) improving passenger facilities; and (2) costs incurred to comply with operational and security requirements under part 139 or part 154 of title 14, Code of Federal Regulations, or part 1542 of title 49, Code of Federal Regulations. (c) Grant requirements In carrying out the program established under this section, the Secretary shall provide not less than 3 and not more than 10 grants to eligible airports in each fiscal year. (d) Eligible airport defined In this section, the term eligible airport means an airport that\u2014 (1) is a general aviation airport or a nonprimary commercial service airport (as determined by the Administrator of the Federal Aviation Administration); and (2) serves a community with a population of at least 75,000. 41782. Authorization of appropriations There is authorized to be appropriated for each fiscal year $50,000,000 to carry out section 41781. .\n##### (b) Technical amendment\nThe analysis for chapter 417 of title 49, United States Code, is amended by inserting after the item relating to section 41767 the following:\nSubchapter IV\u2014Regional Airport Expansion Program 41781. Grants for growing regional airports. 41782. Authorization of appropriations. .",
      "versionDate": "2025-04-29",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-22T16:11:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-29",
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
          "measure-id": "id119hr3085",
          "measure-number": "3085",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-29",
          "originChamber": "HOUSE",
          "update-date": "2025-07-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3085v00",
            "update-date": "2025-07-31"
          },
          "action-date": "2025-04-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Expanding Regional Airports Act</strong></p><p>This bill directs the Department of Transportation (DOT) to establish a grant program for general aviation and nonprimary commercial service airports to improve passenger and flight capacity.</p><p>Grants may be used for (1) activities that improve passenger and flight capacity at the airport, including the expansion of passenger and property screening facilities, runway lengthening, construction of hangars and associated infrastructure, and improving passenger facilities; and (2) costs incurred to comply with certain operational and security requirements.</p><p>DOT must provide 3 to 10 grants per fiscal year to eligible airports (i.e., general aviation or nonprimary commercial service airports that serve a community with a population of at least 75,000).</p>"
        },
        "title": "Expanding Regional Airports Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3085.xml",
    "summary": {
      "actionDate": "2025-04-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expanding Regional Airports Act</strong></p><p>This bill directs the Department of Transportation (DOT) to establish a grant program for general aviation and nonprimary commercial service airports to improve passenger and flight capacity.</p><p>Grants may be used for (1) activities that improve passenger and flight capacity at the airport, including the expansion of passenger and property screening facilities, runway lengthening, construction of hangars and associated infrastructure, and improving passenger facilities; and (2) costs incurred to comply with certain operational and security requirements.</p><p>DOT must provide 3 to 10 grants per fiscal year to eligible airports (i.e., general aviation or nonprimary commercial service airports that serve a community with a population of at least 75,000).</p>",
      "updateDate": "2025-07-31",
      "versionCode": "id119hr3085"
    },
    "title": "Expanding Regional Airports Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expanding Regional Airports Act</strong></p><p>This bill directs the Department of Transportation (DOT) to establish a grant program for general aviation and nonprimary commercial service airports to improve passenger and flight capacity.</p><p>Grants may be used for (1) activities that improve passenger and flight capacity at the airport, including the expansion of passenger and property screening facilities, runway lengthening, construction of hangars and associated infrastructure, and improving passenger facilities; and (2) costs incurred to comply with certain operational and security requirements.</p><p>DOT must provide 3 to 10 grants per fiscal year to eligible airports (i.e., general aviation or nonprimary commercial service airports that serve a community with a population of at least 75,000).</p>",
      "updateDate": "2025-07-31",
      "versionCode": "id119hr3085"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3085ih.xml"
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
      "title": "Expanding Regional Airports Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding Regional Airports Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to establish a program to provide assistance to underserved airports to improve passenger and flight capacity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:35Z"
    }
  ]
}
```
