# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7855?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7855
- Title: GAAME Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7855
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-05-21T08:08:55Z
- Update date including text: 2026-05-21T08:08:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7855",
    "number": "7855",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "V000081",
        "district": "7",
        "firstName": "Nydia",
        "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
        "lastName": "Vel\u00e1zquez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "GAAME Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:55Z",
    "updateDateIncludingText": "2026-05-21T08:08:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
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
      "actionCode": "Intro-H",
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T15:02:25Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "DC"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NV"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7855ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7855\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2026 Ms. Vel\u00e1zquez (for herself, Ms. Clarke of New York , Mrs. McIver , Ms. Norton , Ms. Titus , Mr. Davis of Illinois , and Mr. Evans of Pennsylvania ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Elementary and Secondary Education Act of 1965 to expand access to school-wide arts and music programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guarantee Access to Arts and Music Education Act of 2026 or the GAAME Act of 2026 .\n#### 2. School-wide access to arts education\nSection 1114 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6314 ) is amended\u2014\n**(1)**\nin subsection (b)(7)(A)(iii)\u2014\n**(A)**\nin subclauses (IV) and (V), by striking ; and and inserting a semicolon; and\n**(B)**\nby adding at the end the following:\n(VI) sequential, standards-based arts education taught by certified arts educators (as defined by the State) and community arts providers to meet the challenging State academic standards; and ; and\n**(2)**\nby adding at the end the following:\n(f) Definition of arts For purposes of subsection (b)(7)(A)(iii)(VI), the term arts means dance, media arts, theater, and visual arts. .\n#### 3. School-wide access to music education\nSection 1114(b)(7)(A)(iii) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6314(b)(7)(A)(iii) ), as amended by section (2), is further amended by inserting after subclause (VI) the following:\n(VII) sequential, standards-based music education that is aligned to challenging State academic standards and is taught by certified music educators (as defined by the State); and .\n#### 4. Targeted assistance schools for arts education\nSection 1115 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6315 ) is amended\u2014\n**(1)**\nin subsection (b)(2)(A), by striking well-rounded education; inserting the following:\nwell-rounded education, such as\u2014 (i) programmatic assistance for students to participate in arts programs that address their academic needs (including support for certified arts educators (as defined by the State), arts educator professional development, supplies, and other expenses associated with instruction in the arts); and ; and\n**(2)**\nby adding at the end the following:\n(i) Definition of arts For purposes of subsection (b)(2)(A)(i), the term arts means dance, media arts, theater, and visual arts. .\n#### 5. Targeted assistance schools for music education\nSection 1115(b)(2)(A) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6315(b)(2)(A) ), as amended by section 4, is further amended by adding at the end the following:\n(ii) programmatic assistance for students to participate in music programs that address their academic needs (including support for certified music educators, music educator professional development, instruments, sheet music, music technology, and other expenses associated with music instruction); .",
      "versionDate": "2026-03-05",
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
        "actionDate": "2026-03-05",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4018",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "GAAME Act of 2026",
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
        "name": "Education",
        "updateDate": "2026-04-02T18:20:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-05",
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
          "measure-id": "id119hr7855",
          "measure-number": "7855",
          "measure-type": "hr",
          "orig-publish-date": "2026-03-05",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7855v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2026-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Guarantee Access to Arts and Music Education Act of 2026 or the GAAME Act of 2026</strong></p><p>This bill specifies that funds that support the instructional needs of elementary and secondary students from low-income families (i.e., Title I funds) may be used for arts and music programs.</p><p>First, the bill specifies that schools operating school-wide programs may include descriptions related to arts and music education in their comprehensive plans. Such a plan may include a description of (1) how sequential, standards-based arts education taught by certified educators and providers meet the challenging state academic standards, and (2) how sequential, standards-based music education taught by certified educators align with the challenging state academic standards.</p><p>Second, the bill specifies that schools operating targeted assistance programs may use funds for arts and music programs that address the academic needs of students. This assistance may include providing support for certified educators, professional development, supplies, instruments, and other expenses.</p>"
        },
        "title": "GAAME Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7855.xml",
    "summary": {
      "actionDate": "2026-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Guarantee Access to Arts and Music Education Act of 2026 or the GAAME Act of 2026</strong></p><p>This bill specifies that funds that support the instructional needs of elementary and secondary students from low-income families (i.e., Title I funds) may be used for arts and music programs.</p><p>First, the bill specifies that schools operating school-wide programs may include descriptions related to arts and music education in their comprehensive plans. Such a plan may include a description of (1) how sequential, standards-based arts education taught by certified educators and providers meet the challenging state academic standards, and (2) how sequential, standards-based music education taught by certified educators align with the challenging state academic standards.</p><p>Second, the bill specifies that schools operating targeted assistance programs may use funds for arts and music programs that address the academic needs of students. This assistance may include providing support for certified educators, professional development, supplies, instruments, and other expenses.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr7855"
    },
    "title": "GAAME Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Guarantee Access to Arts and Music Education Act of 2026 or the GAAME Act of 2026</strong></p><p>This bill specifies that funds that support the instructional needs of elementary and secondary students from low-income families (i.e., Title I funds) may be used for arts and music programs.</p><p>First, the bill specifies that schools operating school-wide programs may include descriptions related to arts and music education in their comprehensive plans. Such a plan may include a description of (1) how sequential, standards-based arts education taught by certified educators and providers meet the challenging state academic standards, and (2) how sequential, standards-based music education taught by certified educators align with the challenging state academic standards.</p><p>Second, the bill specifies that schools operating targeted assistance programs may use funds for arts and music programs that address the academic needs of students. This assistance may include providing support for certified educators, professional development, supplies, instruments, and other expenses.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr7855"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7855ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Elementary and Secondary Education Act of 1965 to expand access to school-wide arts and music programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:32Z"
    },
    {
      "title": "GAAME Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GAAME Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Guarantee Access to Arts and Music Education Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:19Z"
    }
  ]
}
```
