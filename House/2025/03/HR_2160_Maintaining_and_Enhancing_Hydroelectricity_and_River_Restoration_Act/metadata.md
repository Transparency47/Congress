# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2160?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2160
- Title: Maintaining and Enhancing Hydroelectricity and River Restoration Act
- Congress: 119
- Bill type: HR
- Bill number: 2160
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-04-29T08:07:00Z
- Update date including text: 2026-04-29T08:07:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2160",
    "number": "2160",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001172",
        "district": "3",
        "firstName": "Adrian",
        "fullName": "Rep. Smith, Adrian [R-NE-3]",
        "lastName": "Smith",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Maintaining and Enhancing Hydroelectricity and River Restoration Act",
    "type": "HR",
    "updateDate": "2026-04-29T08:07:00Z",
    "updateDateIncludingText": "2026-04-29T08:07:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:01:05Z",
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
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "WA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "PA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "WA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "NY"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NH"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "NY"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "WV"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "KS"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "NE"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "KS"
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
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NH"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "NE"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "WA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "AL"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "MA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2160ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2160\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Smith of Nebraska (for himself, Ms. DelBene , Mr. Fitzpatrick , Ms. Schrier , Ms. Tenney , and Ms. Goodlander ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to support upgrades at existing hydroelectric dams in order to increase clean energy production, improve the resiliency and reliability of the United States electric grid, enhance the health of the Nation\u2019s rivers and associated wildlife habitats, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Maintaining and Enhancing Hydroelectricity and River Restoration Act .\n#### 2. Credit for maintaining and enhancing hydroelectric facilities\n##### (a) In general\nSubpart E of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 48E the following new section:\n48F. Credit for maintaining and enhancing hydroelectric facilities (a) In general For purposes of section 46, the credit for maintaining and enhancing hydroelectric facilities for any taxable year is an amount equal to 30 percent of the basis of any hydropower improvement property placed in service during such taxable year. (b) Certain progress expenditure rules made applicable Rules similar to the rules of subsections (c)(4) and (d) of section 46 (as in effect on the day before the date of the enactment of the Revenue Reconciliation Act of 1990) shall apply for purposes of subsection (a). (c) Hydropower improvement property In this section, the term hydropower improvement property means property\u2014 (1) which\u2014 (A) adds or improves fish passage at a qualified dam, (B) maintains or improves the quality of the water retained or released by a qualified dam, (C) promotes downstream sediment transport processes and habitat maintenance with respect to a qualified dam, (D) upgrades, repairs, or reconstructs a qualified dam to meet Federal dam safety and security standards, (E) improves the public uses of, and access to, public waterways impacted by a qualified dam in a manner consistent with a license issued by the Federal Energy Regulatory Commission or a settlement agreement related to such a license, (F) removes an obsolete river obstruction, or (G) places into service an approved remote dam, and (2) for which, prior to January 1, 2032, the taxpayer receives written approval with respect to any property described in paragraph (1) from the Federal Energy Regulatory Commission or State or local officials, as appropriate. (d) Other definitions In this section\u2014 (1) Approved remote dam The term approved remote dam means\u2014 (A) a hydroelectric dam which\u2014 (i) exclusively services communities not interconnected to the Electric Reliability Council of Texas, the Eastern Interconnection, or the Western Interconnection, (ii) was licensed by the Federal Energy Regulatory Commission before December 31, 2020, (iii) does not contribute to atmosphere pollution, and (iv) has a maximum net output of not greater than 20 megawatts, and (B) any interconnection property associated with a dam described in subparagraph (A). (2) Fish passage The term fish passage means, with respect to any qualified dam, any new or upgraded turbine, fishway, or other fish passage technology which improves fish migration and survival rates. (3) Interconnection property The term interconnection property means, with respect to any dam described in paragraph (1)(A), any tangible property\u2014 (A) to enable the delivery of electricity from such dam to any customer, and (B) which satisfies the requirements under clauses (ii) and (iii) of section 48(a)(8)(B). (4) Obsolete river obstruction The term obsolete river obstruction means a qualified nonpowered dam (as defined in section 34(e)(3) of the Federal Power Act ( 16 U.S.C. 823e(e)(3) )) no longer serving its intended purpose. (5) Qualified dam The term qualified dam means a hydroelectric dam that is licensed by the Federal Energy Regulatory Commission or legally operating without such a license before the date of enactment of this section. .\n##### (b) Elective payment and transfer of credit\n**(1) Elective payment**\nSection 6417 of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin subsection (b), by adding at the end the following:\n(13) The credit for maintaining and enhancing hydroelectric facilities under section 48F. , and\n**(B)**\nin subsection (d)(1)\u2014\n**(i)**\nin subparagraph (E), by striking (C), or (D) each place it appears and inserting (C), (D), or (E) ,\n**(ii)**\nby redesignating subparagraph (E) (as amended by clause (i)) as subparagraph (F), and\n**(iii)**\nby inserting after subparagraph (D) the following:\n(E) Election with respect to credit for maintaining and enhancing hydroelectric facilities If a taxpayer other than an entity described in subparagraph (A) makes an election under this subparagraph with respect to any taxable year in which such taxpayer has, after December 31, 2022, placed in service hydropower improvement property (as defined in section 48F(c)), such taxpayer shall be treated as an applicable entity for purposes of this section for such taxable year, but only with respect to the credit described in subsection (b)(13). .\n**(2) Transfer**\nSection 6418(f)(1)(A) of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(xii) The credit for maintaining and enhancing hydroelectric facilities under section 48F. .\n##### (c) Conforming amendments\n**(1)**\nSection 46 of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin paragraph (6), by striking and at the end,\n**(B)**\nin paragraph (7), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following:\n(8) the credit for maintaining and enhancing hydroelectric facilities. .\n**(2)**\nSection 49(a)(1)(C) of such Code is amended\u2014\n**(A)**\nin clause (vii), by striking and at the end,\n**(B)**\nin clause (viii), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following:\n(ix) the basis of any hydropower improvement property under section 48F. .\n**(3)**\nSection 50 of such Code is amended\u2014\n**(A)**\nin subsection (a)(2)(E), as amended by section 13702(b) of Public Law 117\u2013169 , by striking or 48E(e) and inserting 48E(e), or 48F(b) , and\n**(B)**\nin subsection (d)(2)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting or any hydropower improvement property (as defined in section 48F(c)) after any energy storage technology (as defined in section 48(c)(6)) , and\n**(ii)**\nin subparagraph (B), by striking energy storage technology each place it appears and inserting energy storage technology or hydropower improvement property .\n**(4)**\nThe table of sections for subpart E of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 48E the following new item:\nSec. 48F. Credit for maintaining and enhancing hydroelectric facilities. .\n##### (d) Effective date\nThe amendments made by this section shall apply to property placed in service after December 31, 2022.",
      "versionDate": "2025-03-14",
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
        "actionDate": "2025-03-27",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1183",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Maintaining and Enhancing Hydroelectricity and River Restoration Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-05-08T20:02:20Z"
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
          "measure-id": "id119hr2160",
          "measure-number": "2160",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2160v00",
            "update-date": "2025-05-14"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Maintaining and Enhancing Hydroelectricity and River Restoration Act</strong></p><p>This bill establishes a new investment tax credit in the amount of 30% of the basis of any hydropower improvement property.</p><p>The bill defines <em>hydropower improvement property</em> as property that</p><ul><li>adds or improves fish passage at a qualified dam;</li><li>maintains or improves the quality of the water retained or released by a qualified dam;</li><li>promotes downstream sediment transport and habitat maintenance;</li><li>upgrades, repairs, or reconstructs a qualified dam to meet safety and security standards;</li><li>improves public uses of, and access to, public waterways impacted by a qualified dam;</li><li>removes an obsolete river obstruction; or</li><li>places into service an approved remote dam.</li></ul><p>Further, written approval for hydropower improvement property must be obtained from the Federal Energy Regulatory Commission or state or local officials prior to January 1, 2032.</p><p>The bill also allows an election to claim the investment tax credit for qualified progress expenses for some types of hydropower improvement property in advance of such property being placed into service. Any investment tax credit amount claimed for qualified progress expenses reduces the amount of the investment tax credit that may be claimed once the hydropower improvement property is placed into service.\u00a0</p><p>The bill authorizes certain entities, including tax-exempt and governmental entities, to treat the investment tax credit for hydropower improvement property as a payment of tax and receive a refund of any overpayment (also known as elective pay).\u00a0</p><p>Finally, the investment tax credit for hydropower improvement property may be transferred (i.e., sold).</p><p>\u00a0</p>"
        },
        "title": "Maintaining and Enhancing Hydroelectricity and River Restoration Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2160.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Maintaining and Enhancing Hydroelectricity and River Restoration Act</strong></p><p>This bill establishes a new investment tax credit in the amount of 30% of the basis of any hydropower improvement property.</p><p>The bill defines <em>hydropower improvement property</em> as property that</p><ul><li>adds or improves fish passage at a qualified dam;</li><li>maintains or improves the quality of the water retained or released by a qualified dam;</li><li>promotes downstream sediment transport and habitat maintenance;</li><li>upgrades, repairs, or reconstructs a qualified dam to meet safety and security standards;</li><li>improves public uses of, and access to, public waterways impacted by a qualified dam;</li><li>removes an obsolete river obstruction; or</li><li>places into service an approved remote dam.</li></ul><p>Further, written approval for hydropower improvement property must be obtained from the Federal Energy Regulatory Commission or state or local officials prior to January 1, 2032.</p><p>The bill also allows an election to claim the investment tax credit for qualified progress expenses for some types of hydropower improvement property in advance of such property being placed into service. Any investment tax credit amount claimed for qualified progress expenses reduces the amount of the investment tax credit that may be claimed once the hydropower improvement property is placed into service.\u00a0</p><p>The bill authorizes certain entities, including tax-exempt and governmental entities, to treat the investment tax credit for hydropower improvement property as a payment of tax and receive a refund of any overpayment (also known as elective pay).\u00a0</p><p>Finally, the investment tax credit for hydropower improvement property may be transferred (i.e., sold).</p><p>\u00a0</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr2160"
    },
    "title": "Maintaining and Enhancing Hydroelectricity and River Restoration Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Maintaining and Enhancing Hydroelectricity and River Restoration Act</strong></p><p>This bill establishes a new investment tax credit in the amount of 30% of the basis of any hydropower improvement property.</p><p>The bill defines <em>hydropower improvement property</em> as property that</p><ul><li>adds or improves fish passage at a qualified dam;</li><li>maintains or improves the quality of the water retained or released by a qualified dam;</li><li>promotes downstream sediment transport and habitat maintenance;</li><li>upgrades, repairs, or reconstructs a qualified dam to meet safety and security standards;</li><li>improves public uses of, and access to, public waterways impacted by a qualified dam;</li><li>removes an obsolete river obstruction; or</li><li>places into service an approved remote dam.</li></ul><p>Further, written approval for hydropower improvement property must be obtained from the Federal Energy Regulatory Commission or state or local officials prior to January 1, 2032.</p><p>The bill also allows an election to claim the investment tax credit for qualified progress expenses for some types of hydropower improvement property in advance of such property being placed into service. Any investment tax credit amount claimed for qualified progress expenses reduces the amount of the investment tax credit that may be claimed once the hydropower improvement property is placed into service.\u00a0</p><p>The bill authorizes certain entities, including tax-exempt and governmental entities, to treat the investment tax credit for hydropower improvement property as a payment of tax and receive a refund of any overpayment (also known as elective pay).\u00a0</p><p>Finally, the investment tax credit for hydropower improvement property may be transferred (i.e., sold).</p><p>\u00a0</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr2160"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2160ih.xml"
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
      "title": "Maintaining and Enhancing Hydroelectricity and River Restoration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:46Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Maintaining and Enhancing Hydroelectricity and River Restoration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to support upgrades at existing hydroelectric dams in order to increase clean energy production, improve the resiliency and reliability of the United States electric grid, enhance the health of the Nation's rivers and associated wildlife habitats, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:33:41Z"
    }
  ]
}
```
