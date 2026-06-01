# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4018?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4018
- Title: GAAME Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4018
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-04-03T15:47:49Z
- Update date including text: 2026-04-03T15:47:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4018",
    "number": "4018",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "GAAME Act of 2026",
    "type": "S",
    "updateDate": "2026-04-03T15:47:49Z",
    "updateDateIncludingText": "2026-04-03T15:47:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T21:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NM"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4018is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4018\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mr. Booker (for himself, Mr. Luj\u00e1n , and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Elementary and Secondary Education Act of 1965 to expand access to school-wide arts and music programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guarantee Access to Arts and Music Education Act of 2026 or the GAAME Act of 2026 .\n#### 2. School-wide access to arts education\nSection 1114(b)(7)(A)(iii) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6314(b)(7)(A)(iii) ) is amended\u2014\n**(1)**\nin subclause (IV) and (V), by striking ; and and inserting a semicolon; and\n**(2)**\nby adding at the end the following:\n(VI) sequential, standards-based arts education (which may include dance, media arts, theater, and visual arts) taught by certified arts educators (as defined by the State) and community arts providers to meet the challenging State academic standards; and .\n#### 3. School-wide access to music education\nSection 1114(b)(7)(A)(iii) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6314(b)(7)(A)(iii) ), as amended by section (2), is further amended by inserting after subclause (VI) the following:\n(VII) sequential, standards-based music education that is aligned to challenging State academic standards and is taught by certified music educators (as defined by the State); and .\n#### 4. Targeted assistance schools for arts education\nSection 1115 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6315 ) is amended\u2014\n**(1)**\nin subsection (b)(2)(A), by striking well-rounded education; inserting the following:\nwell rounded education, such as\u2014 (i) programmatic assistance for students to participate in arts programs that address their academic needs (including support for certified arts educators (as defined by the State), arts educator professional development, supplies, and other expenses associated with instruction in the arts); and ; and\n**(2)**\nby adding at the end the following:\n(i) Definition of arts For purposes of subsection (b)(2)(A)(i), the term arts means dance, media arts, theater, and visual arts. .\n#### 5. Targeted assistance schools for music education\nSection 1115(b)(2)(A) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6315(b)(2)(A) ), as amended by section 4, is further amended by adding at the end the following:\n(ii) programmatic assistance for students to participate in music programs that address their academic needs (including support for certified music educators, music educator professional development, instruments, sheet music, music technology, and other expenses associated with music instruction); .",
      "versionDate": "2026-03-05",
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
        "actionDate": "2026-03-05",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "7855",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "GAAME Act of 2026",
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
        "name": "Education",
        "updateDate": "2026-03-24T17:41:39Z"
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
          "measure-id": "id119s4018",
          "measure-number": "4018",
          "measure-type": "s",
          "orig-publish-date": "2026-03-05",
          "originChamber": "SENATE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4018v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2026-03-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Guarantee Access to Arts and Music Education Act of 2026 or the GAAME Act of 2026</strong></p><p>This bill specifies that funds that support the instructional needs of elementary and secondary students from low-income families (i.e., Title I funds) may be used for arts and music programs.</p><p>First, the bill specifies that schools operating school-wide programs may include descriptions related to arts and music education in their comprehensive plans. Such a plan may include a description of (1) how sequential, standards-based arts education taught by certified educators and providers meet the challenging state academic standards, and (2) how sequential, standards-based music education taught by certified educators align with the challenging state academic standards.</p><p>Second, the bill specifies that schools operating targeted assistance programs may use funds for arts and music programs that address the academic needs of students. This assistance may include providing support for certified educators, professional development, supplies, instruments, and other expenses.</p>"
        },
        "title": "GAAME Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4018.xml",
    "summary": {
      "actionDate": "2026-03-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Guarantee Access to Arts and Music Education Act of 2026 or the GAAME Act of 2026</strong></p><p>This bill specifies that funds that support the instructional needs of elementary and secondary students from low-income families (i.e., Title I funds) may be used for arts and music programs.</p><p>First, the bill specifies that schools operating school-wide programs may include descriptions related to arts and music education in their comprehensive plans. Such a plan may include a description of (1) how sequential, standards-based arts education taught by certified educators and providers meet the challenging state academic standards, and (2) how sequential, standards-based music education taught by certified educators align with the challenging state academic standards.</p><p>Second, the bill specifies that schools operating targeted assistance programs may use funds for arts and music programs that address the academic needs of students. This assistance may include providing support for certified educators, professional development, supplies, instruments, and other expenses.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119s4018"
    },
    "title": "GAAME Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-03-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Guarantee Access to Arts and Music Education Act of 2026 or the GAAME Act of 2026</strong></p><p>This bill specifies that funds that support the instructional needs of elementary and secondary students from low-income families (i.e., Title I funds) may be used for arts and music programs.</p><p>First, the bill specifies that schools operating school-wide programs may include descriptions related to arts and music education in their comprehensive plans. Such a plan may include a description of (1) how sequential, standards-based arts education taught by certified educators and providers meet the challenging state academic standards, and (2) how sequential, standards-based music education taught by certified educators align with the challenging state academic standards.</p><p>Second, the bill specifies that schools operating targeted assistance programs may use funds for arts and music programs that address the academic needs of students. This assistance may include providing support for certified educators, professional development, supplies, instruments, and other expenses.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119s4018"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4018is.xml"
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
      "title": "GAAME Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T02:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GAAME Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guarantee Access to Arts and Music Education Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Elementary and Secondary Education Act of 1965 to expand access to school-wide arts and music programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:18:27Z"
    }
  ]
}
```
