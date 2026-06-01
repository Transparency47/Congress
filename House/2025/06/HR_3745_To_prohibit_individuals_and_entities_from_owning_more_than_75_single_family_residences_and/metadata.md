# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3745?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3745
- Title: American Neighborhoods Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3745
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2025-06-30T15:45:46Z
- Update date including text: 2025-06-30T15:45:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-05 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-05 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3745",
    "number": "3745",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "A000370",
        "district": "12",
        "firstName": "Alma",
        "fullName": "Rep. Adams, Alma S. [D-NC-12]",
        "lastName": "Adams",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "American Neighborhoods Protection Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-30T15:45:46Z",
    "updateDateIncludingText": "2025-06-30T15:45:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-05T14:03:40Z",
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
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NJ"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "LA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MS"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3745ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3745\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Ms. Adams (for herself, Mrs. McIver , Mr. Fields , and Mr. Thompson of Mississippi ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit individuals and entities from owning more than 75 single-family residences, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Neighborhoods Protection Act of 2025 .\n#### 2. Excise tax on certain taxpayers failing to sell excess single-family residences\n##### (a) In general\nSubtitle D of the Internal Revenue Code of 1986 is amended by adding at the end the following new chapter:\n50B Excess Single-Family Residences Sec. 5000E. Excess single-family residences. 5000E. Excess single-family residences (a) In general There is hereby imposed on each covered taxpayer for each taxable year a tax in an amount equal to the product of\u2014 (1) $10,000, and (2) the excess of\u2014 (A) the number of single-family residences owned by the taxpayer as of the last day of the taxable year, over (B) 75. (b) Covered taxpayer For purposes of this section\u2014 (1) In general The term covered taxpayer means a taxpayer that is not\u2014 (A) a mortgage note holder that owns a single-family residence through foreclosure, (B) a organization which is described in subsection 501(c)(3) and exempt from tax under section 501(a), (C) a person primarily engaged in the construction or rehabilitation of single-family residences, or (D) a person who owns federally subsidized housing. (2) Aggregation rules (A) In general For purposes of this section, all persons which are treated as a single employer under subsections (a) and (b) of section 52 shall be treated as a single taxpayer. (B) Modifications For purposes of this paragraph\u2014 (i) section 52(a) shall be applied by substituting component members for members , and (ii) for purposes of applying subsection (b), the term trade or business shall include any activity treated as a trade or business under paragraph (5) or (6) of subsection (c) (determined without regard to the phrase to the extent provided in regulations in such paragraph (6)). (C) Component member For purposes of this paragraph, the term component member has the meaning given such term by section 1563(b), except that the determination shall be made without regard to subsection (b)(2). (c) Other rules and definitions For purposes of this section: (1) Single-family residence The term single-family residence means a residential property consisting not more than 4 dwelling units. (2) Own (A) In general The term own , with respect to a single-family residence, means having a direct majority ownership interest in the single-family residence. (B) Special rule for certain sales (i) In general Notwithstanding subparagraph (A), for purposes of subsections (a)(2)(A), any single-family residence which is owned by a covered taxpayer as of the first day of the taxable year and which is sold or transferred during such taxable year by the covered taxpayer in a sale or transfer described in clause (ii) shall be treated as a single-family residence which is owned by the covered taxpayer as of the last day of such taxable year. (ii) Sales described A sale or transfer is described in this clause if such sale or transfer is a sale or transfer to\u2014 (I) a corporation or entity engaged in a trade or business, (II) a group of more than 2 individuals, or (III) a person who owns any other single-family residence at the time of such sale. (d) Reporting (1) In general The Secretary shall require such reporting as the Secretary determines necessary or appropriate to carry out the purposes of this section, including requiring a certification of the following from each purchaser or transferee of a single-family residence: (A) The name and address of the purchaser or transferee. (B) Identify whether the sale is a sale described in subsection (c)(2)(B)(ii) of the Internal Revenue Code 1986. (2) Failure to report (A) In general Any person who fails to report information required under paragraph (1) or who fails to include correct information in such report shall pay a penalty of $50,000. (B) Reasonable cause waiver No penalty shall be imposed under this paragraph with respect to any failure if it is shown that such failure is due to reasonable cause and not to willful neglect. (C) Treatment of penalty The penalty under this paragraph shall be paid upon notice and demand by the Secretary, and shall be assessed and collected in the same manner as an assessable penalty under subchapter B of chapter 68. .\n##### (b) Clerical amendment\nThe table of chapters for subtitle D of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nChapter 50B\u2014Excess single-Family residences .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 3. Use of tax revenues for down payment assistance grants\n##### (a) Establishment of housing trust fund\n**(1) In general**\nSubchapter A of chapter 98 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n9512. Housing Trust Fund (a) Creation of trust fund There is established in the Treasury of the United States a trust fund to be known as the Housing Trust Fund (hereinafter in this section referred to as the Trust Fund ), consisting of such amounts as may be appropriated or credited to such Trust Fund as provided in this section and section 9602(b). (b) Transfers to Trust Fund There are hereby appropriated to the Housing Trust Fund amounts equivalent to revenues received in the Treasury from the tax imposed by section 5000E. (c) Expenditures from Trust Fund Amounts in the Housing Trust Fund shall be available, as provided in appropriations Acts, only for grants under section 3(b) of the American Neighborhoods Protection Act of 2025. .\n**(2) Clerical amendment**\nThe table of sections for subchapter A of chapter 98 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 9512. Housing Trust Fund. .\n##### (b) Grants program for down payment assistance programs\n**(1) Establishment**\nThe Secretary of Housing and Urban Development shall establish a program under which the Secretary makes grants to State housing finance agencies to establish new or supplement existing programs that provide down payment assistance to families purchasing homes within the State.\n**(2) Priority**\nA State housing finance agency that receives a grant under this section shall give priority to families seeking assistance to purchase any single-family residence that is sold or transferred by a covered taxpayer (as defined in section 5000E(b) of the Internal Revenue Code of 1986, as added by section 2).",
      "versionDate": "2025-06-05",
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
        "name": "Taxation",
        "updateDate": "2025-06-30T15:45:46Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3745ih.xml"
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
      "title": "American Neighborhoods Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Neighborhoods Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit individuals and entities from owning more than 75 single-family residences, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T06:48:43Z"
    }
  ]
}
```
