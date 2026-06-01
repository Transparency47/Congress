# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1183?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1183
- Title: Maintaining and Enhancing Hydroelectricity and River Restoration Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1183
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2026-04-23T11:03:25Z
- Update date including text: 2026-04-23T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1183",
    "number": "1183",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C000127",
        "district": "",
        "firstName": "Maria",
        "fullName": "Sen. Cantwell, Maria [D-WA]",
        "lastName": "Cantwell",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Maintaining and Enhancing Hydroelectricity and River Restoration Act of 2025",
    "type": "S",
    "updateDate": "2026-04-23T11:03:25Z",
    "updateDateIncludingText": "2026-04-23T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-27",
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
        "item": [
          {
            "date": "2025-03-27T18:11:08Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-27T18:11:08Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "AK"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-27",
      "state": "ME"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "ME"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MI"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "AK"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NH"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "WA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NE"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "NE"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "KS"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NH"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1183is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1183\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Ms. Cantwell (for herself, Ms. Murkowski , Mr. King , Ms. Collins , Mr. Peters , Mr. Sullivan , Mrs. Shaheen , Mrs. Murray , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to support upgrades at existing hydroelectric dams in order to increase clean energy production, improve the resiliency and reliability of the United States electric grid, enhance the health of the Nation's rivers and associated wildlife habitats, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Maintaining and Enhancing Hydroelectricity and River Restoration Act of 2025 .\n#### 2. Credit for maintaining and enhancing hydroelectric facilities\n##### (a) In general\nSubpart E of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 48E the following new section:\n48F. Credit for maintaining and enhancing hydroelectric facilities (a) In general For purposes of section 46, the credit for maintaining and enhancing hydroelectric facilities for any taxable year is an amount equal to 30 percent of the basis of any hydropower improvement property placed in service during such taxable year. (b) Certain progress expenditure rules made applicable Rules similar to the rules of subsections (c)(4) and (d) of section 46 (as in effect on the day before the date of the enactment of the Revenue Reconciliation Act of 1990) shall apply for purposes of subsection (a). (c) Hydropower improvement property In this section, the term hydropower improvement property means property\u2014 (1) which\u2014 (A) adds or improves fish passage at a qualified dam, (B) maintains or improves the quality of the water retained or released by a qualified dam, (C) promotes downstream sediment transport processes and habitat maintenance with respect to a qualified dam, (D) upgrades, repairs, or reconstructs a qualified dam to meet Federal dam safety and security standards, (E) improves the public uses of, and access to, public waterways impacted by a qualified dam in a manner consistent with a license issued by the Federal Energy Regulatory Commission or a settlement agreement related to such a license, (F) removes an obsolete river obstruction, or (G) places into service an approved remote dam, and (2) for which, prior to January 1, 2035, the taxpayer receives written approval with respect to any property described in paragraph (1) from the Federal Energy Regulatory Commission or State or local officials, as appropriate. (d) Other definitions In this section\u2014 (1) Approved remote dam The term approved remote dam means\u2014 (A) a hydroelectric dam which\u2014 (i) exclusively services communities not interconnected to the Electric Reliability Council of Texas, the Eastern Interconnection, or the Western Interconnection, (ii) was licensed by the Federal Energy Regulatory Commission before December 31, 2020, (iii) does not contribute to atmosphere pollution, and (iv) has a maximum net output of not greater than 20 megawatts, and (B) any interconnection property associated with a dam described in subparagraph (A). (2) Fish passage The term fish passage means, with respect to any qualified dam, any new or upgraded turbine, fishway, or other fish passage technology which improves fish migration and survival rates. (3) Interconnection property The term interconnection property means, with respect to any dam described in paragraph (1)(A), any tangible property\u2014 (A) to enable the delivery of electricity from such dam to any customer, and (B) which satisfies the requirements under clauses (ii) and (iii) of section 48(a)(8)(B). (4) Obsolete river obstruction The term obsolete river obstruction means a qualified nonpowered dam (as defined in section 34(e)(3) of the Federal Power Act ( 16 U.S.C. 823e(e)(3) )) no longer serving its intended purpose. (5) Qualified dam The term qualified dam means a hydroelectric dam that is licensed by the Federal Energy Regulatory Commission or legally operating without such a license before the date of enactment of this section. .\n##### (b) Elective payment and transfer of credit\n**(1) Elective payment**\nSection 6417 of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin subsection (b), by adding at the end the following:\n(13) The credit for maintaining and enhancing hydroelectric facilities under section 48F. , and\n**(B)**\nin subsection (d)(1)\u2014\n**(i)**\nin subparagraph (E), by striking (C), or (D) each place it appears and inserting (C), (D), or (E) ,\n**(ii)**\nby redesignating subparagraph (E) (as amended by clause (i)) as subparagraph (F), and\n**(iii)**\nby inserting after subparagraph (D) the following:\n(E) Election with respect to credit for maintaining and enhancing hydroelectric facilities If a taxpayer other than an entity described in subparagraph (A) makes an election under this subparagraph with respect to any taxable year in which such taxpayer has, after December 31, 2025, placed in service hydropower improvement property (as defined in section 48F(c)), such taxpayer shall be treated as an applicable entity for purposes of this section for such taxable year, but only with respect to the credit described in subsection (b)(13). .\n**(2) Transfer**\nSection 6418(f)(1)(A) of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(xii) The credit for maintaining and enhancing hydroelectric facilities under section 48F. .\n##### (c) Conforming amendments\n**(1)**\nSection 46 of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin paragraph (6), by striking and at the end,\n**(B)**\nin paragraph (7), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following:\n(8) the credit for maintaining and enhancing hydroelectric facilities. .\n**(2)**\nSection 49(a)(1)(C) of such Code is amended\u2014\n**(A)**\nin clause (vii), by striking and at the end,\n**(B)**\nin clause (viii), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following:\n(ix) the basis of any hydropower improvement property under section 48F. .\n**(3)**\nSection 50 of such Code is amended\u2014\n**(A)**\nin subsection (a)(2)(E), as amended by section 13702(b) of Public Law 117\u2013169 , by striking or 48E(e) and inserting 48E(e), or 48F(b) , and\n**(B)**\nin subsection (d)(2)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting or any hydropower improvement property (as defined in section 48F(c)) after any energy storage technology (as defined in section 48(c)(6)) , and\n**(ii)**\nin subparagraph (B), by striking energy storage technology each place it appears and inserting energy storage technology or hydropower improvement property .\n**(4)**\nThe table of sections for subpart E of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 48E the following new item:\nSec. 48F. Credit for maintaining and enhancing hydroelectric facilities. .\n##### (d) Effective date\nThe amendments made by this section shall apply to property placed in service after December 31, 2025.",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-03-14",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2160",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Maintaining and Enhancing Hydroelectricity and River Restoration Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-08T20:00:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
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
          "measure-id": "id119s1183",
          "measure-number": "1183",
          "measure-type": "s",
          "orig-publish-date": "2025-03-27",
          "originChamber": "SENATE",
          "update-date": "2025-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1183v00",
            "update-date": "2025-05-14"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Maintaining and Enhancing Hydroelectricity and River Restoration Act of 2025</strong></p><p>This bill establishes a new investment tax credit in the amount of 30% of the basis of any hydropower improvement property.</p><p>The bill defines <em>hydropower improvement property</em> as property that</p><ul><li>adds or improves fish passage at a qualified dam;</li><li>maintains or improves the quality of the water retained or released by a qualified dam;</li><li>promotes downstream sediment transport and habitat maintenance;</li><li>upgrades, repairs, or reconstructs a qualified dam to meet safety and security standards;</li><li>improves public uses of, and access to, public waterways impacted by a qualified dam;</li><li>removes an obsolete river obstruction; or</li><li>places into service an approved remote dam.</li></ul><p>Further, written approval for hydropower improvement property must be obtained from the Federal Energy Regulatory Commission or state or local officials prior to January 1, 2035.</p><p>The bill also allows an election to claim the investment tax credit for qualified progress expenses for some types of hydropower improvement property in advance of such property being placed into service. Any investment tax credit amount claimed for qualified progress expenses reduces the amount of the investment tax credit that may be claimed once the hydropower improvement property is placed into service.\u00a0</p><p>The bill authorizes certain entities, including tax-exempt and governmental entities, to treat the investment tax credit for hydropower improvement property as a payment of tax and receive a refund of any overpayment (also known as elective pay).\u00a0</p><p>Finally, the investment tax credit for hydropower improvement property may be transferred (i.e., sold).</p><p>\u00a0</p>"
        },
        "title": "Maintaining and Enhancing Hydroelectricity and River Restoration Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1183.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Maintaining and Enhancing Hydroelectricity and River Restoration Act of 2025</strong></p><p>This bill establishes a new investment tax credit in the amount of 30% of the basis of any hydropower improvement property.</p><p>The bill defines <em>hydropower improvement property</em> as property that</p><ul><li>adds or improves fish passage at a qualified dam;</li><li>maintains or improves the quality of the water retained or released by a qualified dam;</li><li>promotes downstream sediment transport and habitat maintenance;</li><li>upgrades, repairs, or reconstructs a qualified dam to meet safety and security standards;</li><li>improves public uses of, and access to, public waterways impacted by a qualified dam;</li><li>removes an obsolete river obstruction; or</li><li>places into service an approved remote dam.</li></ul><p>Further, written approval for hydropower improvement property must be obtained from the Federal Energy Regulatory Commission or state or local officials prior to January 1, 2035.</p><p>The bill also allows an election to claim the investment tax credit for qualified progress expenses for some types of hydropower improvement property in advance of such property being placed into service. Any investment tax credit amount claimed for qualified progress expenses reduces the amount of the investment tax credit that may be claimed once the hydropower improvement property is placed into service.\u00a0</p><p>The bill authorizes certain entities, including tax-exempt and governmental entities, to treat the investment tax credit for hydropower improvement property as a payment of tax and receive a refund of any overpayment (also known as elective pay).\u00a0</p><p>Finally, the investment tax credit for hydropower improvement property may be transferred (i.e., sold).</p><p>\u00a0</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119s1183"
    },
    "title": "Maintaining and Enhancing Hydroelectricity and River Restoration Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Maintaining and Enhancing Hydroelectricity and River Restoration Act of 2025</strong></p><p>This bill establishes a new investment tax credit in the amount of 30% of the basis of any hydropower improvement property.</p><p>The bill defines <em>hydropower improvement property</em> as property that</p><ul><li>adds or improves fish passage at a qualified dam;</li><li>maintains or improves the quality of the water retained or released by a qualified dam;</li><li>promotes downstream sediment transport and habitat maintenance;</li><li>upgrades, repairs, or reconstructs a qualified dam to meet safety and security standards;</li><li>improves public uses of, and access to, public waterways impacted by a qualified dam;</li><li>removes an obsolete river obstruction; or</li><li>places into service an approved remote dam.</li></ul><p>Further, written approval for hydropower improvement property must be obtained from the Federal Energy Regulatory Commission or state or local officials prior to January 1, 2035.</p><p>The bill also allows an election to claim the investment tax credit for qualified progress expenses for some types of hydropower improvement property in advance of such property being placed into service. Any investment tax credit amount claimed for qualified progress expenses reduces the amount of the investment tax credit that may be claimed once the hydropower improvement property is placed into service.\u00a0</p><p>The bill authorizes certain entities, including tax-exempt and governmental entities, to treat the investment tax credit for hydropower improvement property as a payment of tax and receive a refund of any overpayment (also known as elective pay).\u00a0</p><p>Finally, the investment tax credit for hydropower improvement property may be transferred (i.e., sold).</p><p>\u00a0</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119s1183"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1183is.xml"
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
      "title": "Maintaining and Enhancing Hydroelectricity and River Restoration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Maintaining and Enhancing Hydroelectricity and River Restoration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to support upgrades at existing hydroelectric dams in order to increase clean energy production, improve the resiliency and reliability of the United States electric grid, enhance the health of the Nation's rivers and associated wildlife habitats, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T03:03:31Z"
    }
  ]
}
```
