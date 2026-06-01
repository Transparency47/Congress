# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/310?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/310
- Title: Restoring Energy Market Freedom Act
- Congress: 119
- Bill type: HR
- Bill number: 310
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-05-12T14:29:32Z
- Update date including text: 2026-05-12T14:29:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/310",
    "number": "310",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "P000605",
        "district": "10",
        "firstName": "Scott",
        "fullName": "Rep. Perry, Scott [R-PA-10]",
        "lastName": "Perry",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Restoring Energy Market Freedom Act",
    "type": "HR",
    "updateDate": "2026-05-12T14:29:32Z",
    "updateDateIncludingText": "2026-05-12T14:29:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:37:50Z",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "AZ"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TN"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr310ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 310\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Perry (for himself, Mr. Biggs of Arizona , Mr. Ogles , and Mr. Roy ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to repeal certain credits.\n#### 1. Short title\nThis Act may be cited as the Restoring Energy Market Freedom Act .\n#### 2. Repeal of credits\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by striking sections 45, 45J, 45Q, 45U, 45V, 45X, 45Y, 48, 48A, 48B, 48C, 48D, and 48E (and by striking the items relating to such sections in the table of sections for such subpart).\n##### (b) General business credit\nSection 38 of such Code is amended\u2014\n**(1)**\nin subsection (b), by striking paragraphs (8), (21), (29), (36), (37), (38), and (39) and redesignating paragraphs (9)\u2013(20), (22)\u2013(28), (30)\u2013(35), and (40)\u2013(41) as paragraphs (8)\u2013(19), (20)\u2013(26), (27)\u2013(32), and (33)\u2013(34), respectively, and\n**(2)**\nin subsection (c)(4)(B), by striking clauses (iv), (v), and (x) and redesignating clauses (vi)\u2013(ix) and (xi)\u2013(xii) as clauses (iv)\u2013(vii) and (viii)\u2013(ix), respectively.\n##### (c) Conforming amendments\n**(1)**\nSection 25(e)(3) of such Code is amended by adding (as in effect immediately before its repeal) before the period at the end.\n**(2)**\nSection 30C of such Code is amended\u2014\n**(A)**\nin subsection (g)(2)(B), by inserting (as in effect immediately prior to its repeal) after section 45(b)(7)(B) , and\n**(B)**\nin subsection (g)(3), by inserting (as in effect immediately prior to its repeal) after section 45(b)(8) .\n**(3)**\nSection 45K(b)(3) of such Code is amended by striking (within the meaning of section 48(a)(4)(C)) and inserting (within the meaning of section 48(a)(4)(C) as in effect immediately before its repeal) .\n**(4)**\nSection 45K(g)(2) of such Code is amended by striking subparagraph (E).\n**(5)**\nSection 45L(g)(2)(B) of such Code is amended by inserting (as in effect immediately prior to its repeal) after section 45(b)(7)(B) .\n**(6)**\nSection 45Z of such Code is amended\u2014\n**(A)**\nin subsection (c), by inserting (as in effect immediately prior to its repeal) after pursuant to section 45Y(c) ,\n**(B)**\nby amending subsection (d)(4) to read as follows:\n(4) Qualified facility The term qualified facility means a facility used for the production of transportation fuels. , and\n**(C)**\nin subsection (f)\u2014\n**(i)**\nin paragraph (5), by inserting (as in effect immediately prior to its repeal) after section 45Y(g)(6) ,\n**(ii)**\nin paragraph (6), by inserting (as in effect immediately prior to its repeal) after section 45(b)(7) , and\n**(iii)**\nin paragraph (7), by inserting (as in effect immediately prior to its repeal) after section 45(b)(8) .\n**(7)**\nSection 49(a)(C) of such Code is amended by adding and at the end of clause (i), by striking the comma at the end of clause (ii) and inserting a period, and by striking clauses (ii), (iv), (v), and (vi).\n**(8)**\nSection 50(a)(2)(E) of such Code is amended by striking section 48(b) .\n**(9)**\nSection 50(a) of such Code is amended\u2014\n**(A)**\nin paragraph (2), by striking subparagraph (E), and\n**(B)**\nby striking paragraph (3).\n**(10)**\nSection 56A(c) of such Code is amended by striking paragraph (9).\n**(11)**\nSection 59A(b)(4) of such Code is amended by striking properly allocable to and all that follows through the period and by inserting properly allocable to the low-income housing credit determined under section 42(a). .\n**(12)**\nSection 142(o) of such Code is amended by inserting as in effect immediately prior to its repeal after (as defined in section 45Q(e)(3) .\n**(13)**\nSection 168(e)(3)(B) of such Code is amended\u2014\n**(A)**\nin clause (v), by adding and at the end, and\n**(B)**\nby striking clause (vi).\n**(14)**\nSection 179D(b) of such Code is amended\u2014\n**(A)**\nin paragraph (4)(B), by inserting (as in effect immediately prior to its repeal) after section 45(b)(7)(B) , and\n**(B)**\nin paragraph (5), by inserting (as in effect immediately prior to its repeal) after section 45(b)(8) .\n**(15)**\nSection 409 of such Code is amended\u2014\n**(A)**\nin subsection (g), by striking section 48(n)(1) or and section 48(n)(1) and , and\n**(B)**\nin subsection (m), by striking , or subparagraph (A) or (B) of section 48(n)(1) .\n**(16)**\nSection 501(c)(12) of such Code is amended by striking subparagraph (I) and by redesignating subparagraph (J) as subparagraph (I).\n**(17)**\nSection 6417 of such Code is amended\u2014\n**(A)**\nin subsection (b), by striking paragraphs (2), (3), (4), (5), (7), (8), (10), (11), and (12) and by redesignating paragraphs (6) and (9) as paragraphs (2) and (3), respectively, and\n**(B)**\nin subsection (d)\u2014\n**(i)**\nby amending paragraph (1) to read as follows:\n(1) Applicable entity The term applicable entity means\u2014 (A) any organization exempt from the tax imposed by subtitle A, (B) any State or political subdivision thereof, (C) the Tennessee Valley Authority, (D) an Indian tribal government (as defined in section 30D(g)(9)), (E) any Alaska Native Corporation (as defined in section 3 of the Alaska Native Claims Settlement Act ( 43 U.S.C. 1602(m) ), or (F) any corporation operating on a cooperative basis which is engaged in furnishing electric energy to persons in rural areas. , and\n**(ii)**\nby amending paragraph (3) to read as follows:\n(3) Elections (A) Due date Any election under subsection (a) shall be made not later than\u2014 (i) in the case of any government, or political subdivision, described in paragraph (1) and for which no return is required under section 6011 or 6033(a), such date as is determined appropriate by the Secretary, or (ii) in any other case, the due date (including extensions of time) for the return of tax for the taxable year for which the election is made, but in no event earlier than 180 days after the date of the enactment of this section. (B) Additional rules Any election under subsection (a), once made, shall be irrevocable and shall apply (except as otherwise provided in this paragraph) with respect to any credit for the taxable year for which the election is made. .\n**(18)**\nSection 6418(f)(1) of such Code is amended\u2014\n**(A)**\nin subparagraph (A), by striking clauses (ii)\u2013(vii) and (ix)\u2013(xi) and by redesignating clause (viii) as clause (ii),\n**(B)**\nby striking subparagraph (B), and\n**(C)**\nby redesignating subparagraph (C) as subparagraph (B).\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-01-09",
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
        "updateDate": "2025-02-14T16:47:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr310",
          "measure-number": "310",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2026-05-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr310v00",
            "update-date": "2026-05-12"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Restoring Energy Market Freedom Act</strong></p><p>This bill repeals multiple business tax credits related to the production and sale of energy.</p><p>Specifically, the bill repeals the</p><ul><li>renewable electricity production tax credit (for electricity using wind, solar, or other specific types of renewable energy produced by a qualified facility for which construction began before 2025);</li><li>clean electricity production tax credit (for electricity produced\u00a0using a qualified facility that has no greenhouse gas emissions and was\u00a0placed into service in 2025 or after);</li><li>advanced nuclear production tax credit (for electricity produced and sold by a qualified nuclear power facility placed into service before 2021);</li><li>zero-emission nuclear power production tax credit (for electricity produced and sold by a qualified nuclear power facility between 2024 and 2032);</li><li>carbon sequestration tax credit (for the capture and sequestration of carbon oxide);</li><li>clean hydrogen production tax credit (for clean hydrogen produced at a qualified clean production facility);</li><li>advanced manufacturing production tax credit (for the production and sale of qualified\u00a0components, including solar and wind energy components);</li><li>energy investment tax credit (for investments in certain qualified energy property placed into service before 2025);</li><li>clean electricity investment credit (for investments in qualified energy property placed into service in 2025 or after);</li><li>qualifying advance coal project tax credit (for investments in qualifying advanced coal projects),</li><li>clean coal investment tax credit (for investments in qualifying gasification projects);</li><li>advanced energy project tax credit (for investments in qualifying advanced energy projects); and</li><li>advanced manufacturing investment tax credit (for investments in semiconductor or semiconductor manufacturing equipment).</li></ul><p>\u00a0</p>"
        },
        "title": "Restoring Energy Market Freedom Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr310.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Restoring Energy Market Freedom Act</strong></p><p>This bill repeals multiple business tax credits related to the production and sale of energy.</p><p>Specifically, the bill repeals the</p><ul><li>renewable electricity production tax credit (for electricity using wind, solar, or other specific types of renewable energy produced by a qualified facility for which construction began before 2025);</li><li>clean electricity production tax credit (for electricity produced\u00a0using a qualified facility that has no greenhouse gas emissions and was\u00a0placed into service in 2025 or after);</li><li>advanced nuclear production tax credit (for electricity produced and sold by a qualified nuclear power facility placed into service before 2021);</li><li>zero-emission nuclear power production tax credit (for electricity produced and sold by a qualified nuclear power facility between 2024 and 2032);</li><li>carbon sequestration tax credit (for the capture and sequestration of carbon oxide);</li><li>clean hydrogen production tax credit (for clean hydrogen produced at a qualified clean production facility);</li><li>advanced manufacturing production tax credit (for the production and sale of qualified\u00a0components, including solar and wind energy components);</li><li>energy investment tax credit (for investments in certain qualified energy property placed into service before 2025);</li><li>clean electricity investment credit (for investments in qualified energy property placed into service in 2025 or after);</li><li>qualifying advance coal project tax credit (for investments in qualifying advanced coal projects),</li><li>clean coal investment tax credit (for investments in qualifying gasification projects);</li><li>advanced energy project tax credit (for investments in qualifying advanced energy projects); and</li><li>advanced manufacturing investment tax credit (for investments in semiconductor or semiconductor manufacturing equipment).</li></ul><p>\u00a0</p>",
      "updateDate": "2026-05-12",
      "versionCode": "id119hr310"
    },
    "title": "Restoring Energy Market Freedom Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Restoring Energy Market Freedom Act</strong></p><p>This bill repeals multiple business tax credits related to the production and sale of energy.</p><p>Specifically, the bill repeals the</p><ul><li>renewable electricity production tax credit (for electricity using wind, solar, or other specific types of renewable energy produced by a qualified facility for which construction began before 2025);</li><li>clean electricity production tax credit (for electricity produced\u00a0using a qualified facility that has no greenhouse gas emissions and was\u00a0placed into service in 2025 or after);</li><li>advanced nuclear production tax credit (for electricity produced and sold by a qualified nuclear power facility placed into service before 2021);</li><li>zero-emission nuclear power production tax credit (for electricity produced and sold by a qualified nuclear power facility between 2024 and 2032);</li><li>carbon sequestration tax credit (for the capture and sequestration of carbon oxide);</li><li>clean hydrogen production tax credit (for clean hydrogen produced at a qualified clean production facility);</li><li>advanced manufacturing production tax credit (for the production and sale of qualified\u00a0components, including solar and wind energy components);</li><li>energy investment tax credit (for investments in certain qualified energy property placed into service before 2025);</li><li>clean electricity investment credit (for investments in qualified energy property placed into service in 2025 or after);</li><li>qualifying advance coal project tax credit (for investments in qualifying advanced coal projects),</li><li>clean coal investment tax credit (for investments in qualifying gasification projects);</li><li>advanced energy project tax credit (for investments in qualifying advanced energy projects); and</li><li>advanced manufacturing investment tax credit (for investments in semiconductor or semiconductor manufacturing equipment).</li></ul><p>\u00a0</p>",
      "updateDate": "2026-05-12",
      "versionCode": "id119hr310"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr310ih.xml"
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
      "title": "Restoring Energy Market Freedom Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restoring Energy Market Freedom Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to repeal certain credits.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:29Z"
    }
  ]
}
```
