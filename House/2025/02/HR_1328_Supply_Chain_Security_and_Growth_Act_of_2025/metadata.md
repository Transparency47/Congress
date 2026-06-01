# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1328?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1328
- Title: Supply Chain Security and Growth Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1328
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-05-01T16:19:26Z
- Update date including text: 2026-05-01T16:19:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1328",
    "number": "1328",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Supply Chain Security and Growth Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-01T16:19:26Z",
    "updateDateIncludingText": "2026-05-01T16:19:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:08:20Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "PA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jos\u00e9",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "PR"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "IL"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "FL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
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
      "sponsorshipDate": "2025-09-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1328ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1328\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Ms. Malliotakis (for herself, Mr. Panetta , Mr. Buchanan , Ms. Vel\u00e1zquez , Mr. Kelly of Pennsylvania , Mr. Hern\u00e1ndez , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish the critical supply chains reshoring investment tax credit.\n#### 1. Short title\nThis Act may be cited as the Supply Chain Security and Growth Act of 2025 .\n#### 2. Critical supply chains reshoring investment credit\n##### (a) In general\nSubpart E of part IV of subchapter A of the Internal Revenue Code of 1986 is amended by inserting after section 48E the following new section:\n48F. Critical supply chains reshoring investment credit (a) In general For purposes of section 46, in the case of a qualifying taxpayer, the critical supply chains reshoring investment credit is an amount equal to 40 percent of the qualified investment with respect to any critical supply chain facility placed in service during such taxable year. (b) Definitions and special rules For purposes of this section\u2014 (1) Qualifying taxpayer (A) In general The term qualifying taxpayer means a taxpayer that is not a prohibited foreign entity. (B) Prohibited foreign entity For purposes of this paragraph, the term prohibited foreign entity means\u2014 (i) any foreign entity of concern (as defined in section 40207(a)(5) of the Infrastructure Investment and Jobs Act), (ii) any entity with respect to which the government of a covered nation has the right or power (directly or indirectly) to appoint or approve the appointment of a covered officer, or (iii) any entity 25 percent or more of the capital or profits interests of which are owned (directly or indirectly) in the aggregate by 1 or more of the following: (I) A covered nation or an entity described in clause (i) or (ii). (II) A citizen, national, or resident of a covered nation. (III) An entity organized under the laws of a covered nation. (C) Covered officer For purposes of this paragraph, the term covered officer means\u2014 (i) any member of the board of directors, board of supervisors, or an equivalent governing body, (ii) the president, senior vice president, chief executive officer, chief operating officer, chief financial officer, or general counsel, or (iii) any individual who performs duties usually associated with a title listed in clause (i) or (ii). (D) Covered nation For purposes of this paragraph, the term covered nation has the meaning given such term in section 4872(d) of title 10, United States Code. (2) Qualified investment The qualified investment with respect to any critical supply chain facility for any taxable year is an amount equal to the basis of any qualified property placed in service by the taxpayer during such taxable year which is part of a such facility. (3) Qualifying property (A) In general The term qualifying property means property\u2014 (i) that is integral to the operation of a critical supply chain facility, (ii) that is tangible property, (iii) with respect to which depreciation (or amortization in lieu of depreciation) is allowable, and (iv) which is\u2014 (I) constructed, reconstructed, or erected by the taxpayer, or (II) acquired by the taxpayer if the original use of such property commences with the taxpayer. (B) Reconstructed property Property shall be treated as reconstructed for purposes of this paragraph if improvements to such property satisfy the substantial improvement test of section 1400Z\u20132(d)(2)(D)(ii). (4) Critical supply chain facility The term critical supply chain facility means a facility\u2014 (A) the primary purpose of which is the manufacturing of\u2014 (i) An active pharmaceutical ingredient (as defined in section 2017.1 of title 21, Code of Federal Regulations (or any successor regulations)), (ii) A drug (as defined in section 201(g) of the Federal Food, Drug, and Cosmetic Act), (iii) A biological product (as defined in section 351(i)(1) of the Public Health Service Act), (iv) A medical countermeasure (as defined in section 319F\u20133(i)(1) of the Public Health Service Act), (v) A medical diagnostic device (as defined in section 201(h) of the Federal Food, Drug, and Cosmetic Act) intended for use in the diagnosis of disease or other conditions, (vi) Semiconductors or semiconductor manufacturing equipment, (vii) Aerospace equipment as defined under North American Industry Classification Code 3364, or (viii) Artificial nanomaterials, and (B) located in\u2014 (i) a specified possession within the meaning of section 937(c), (ii) or Puerto Rico. (5) Aggregation rule (A) In general Members of a qualified affiliated group shall be treated as a single taxpayer. (B) Qualified affiliated group (i) In general The term qualified affiliated group means an affiliated group (as defined in section 1504(a), determined without regard to section 1504(b)(3)) at least 1 member of which has made a qualified investment in a critical supply chain facility located in an economically distressed zone. (ii) Economically distressed zone For purposes of this subparagraph, the term economically distressed zone means a population census tract that\u2014 (I) is a qualified opportunity zone (as defined in section 1400z\u20131(a)), and (II) has a poverty rate of not less than 30 percent. (6) Exemption from certain special rules The credit determined under subsection (a) shall be determined without regard to paragraphs (1) and (4) of section 50(b). .\n##### (b) Coordination between critical supply chains reshoring credit and electricity production credit\nSection 45(e) of such Code is amended by adding at the end the following new subsection:\n(e) Coordination with critical supply chains reshoring investment credit The term qualified facility shall not include any facility if a credit is allowed under section 48F with respect to such facility for the taxable year or any prior taxable year. .\n##### (c) Elective payment allowed\n**(1) In general**\nSection 6417(b) of such Code is amended by adding at the end the following:\n(13) The critical supply chains reshoring investment credit determined under section 48F. .\n**(2) Election to be treated as applicable entity**\nSection 6417(d)(1) is amended\u2014\n**(A)**\nby redesignating subparagraph (E) as subparagraph (F), and\n**(B)**\nby inserting after subparagraph (D) the following new subparagraph:\n(E) Election with respect to critical supply chains reshoring credit If a taxpayer other than an entity described in subparagraph (A) makes an election under this subparagraph with respect to any taxable year in which such taxpayer has placed in service a critical supply chain facility (as defined in section 48F(b)(4)), such taxpayer shall be treated as an applicable entity for purposes of this section for such taxable year, but only with respect to the credit described in subsection (b)(13). .\n##### (d) Credit made transferable\nSection 6418(f)(1)(A) of such Code is amended by adding at the end the following:\n(xii) The critical supply chains reshoring investment credit determined under section 48F. .\n##### (e) Credit included in investment credit\nSection 46 of such Code is amended by striking and at the end of paragraph (6), by striking the period at the end of paragraph (7) and inserting , and , and by adding at the end the following new paragraph:\n(8) the critical supply chains reshoring investment credit. .\n##### (f) Effective date\nThe amendments made by this section shall apply to property placed in service after December 31, 2024.\n#### 3. Increase in deemed credit for taxes paid to possession of the United States\n##### (a) In general\nSection 960(d) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(4) Increase for taxes paid to possession of United States In the case of tested foreign income taxes paid or accrued to a possession of the United States, paragraph (1) shall be applied by substituting 100 percent for 80 percent . .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxes paid or accrued after December 31, 2024.",
      "versionDate": "2025-02-13",
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
        "updateDate": "2025-05-06T14:08:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1328",
          "measure-number": "1328",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2026-05-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1328v00",
            "update-date": "2026-05-01"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Supply Chain Security and Growth Act of 2025</strong></p><p>This bill establishes a tax credit for qualified investments made in certain facilities that are located in a U.S. possession and manufacture drugs, pharmaceuticals, semiconductors, or certain other items, subject to limitations. The bill also increases the deemed-paid foreign tax credit for taxes paid to a U.S. possession.</p><p>Specifically, under the bill, a taxpayer (other than a prohibited foreign entity) is allowed a tax credit for 40% of an investment in certain property that is</p><ul><li>placed into service during the tax year;</li><li>integral to the operation of a critical supply chain facility; and</li><li>constructed, reconstructed, or erected by the taxpayer, or property acquired for original used by the taxpayer.</li></ul><p>The bill defines <em>critical supply chain facility</em> as a facility that (1) manufactures active pharmaceutical ingredients, drugs, biologic products, medical countermeasures, medical diagnostic devices, semiconductors, semiconductor manufacturing equipment, aerospace equipment, or artificial nanomaterials; and (2) is located in Puerto Rico, Guam, American Samoa, the Northern Mariana Islands, or the Virgin Islands.</p><p>Under the bill, the tax credit is transferable and may be claimed as a direct cash payment (i.e., elective payment). (Limitations apply.)</p><p>Finally, the bill increases to 100% (from 80%) the deemed-paid foreign tax credit for income taxes paid or accrued by a controlled foreign corporation (CFC) to a U.S. possession. (Under current law, a U.S. shareholder of a CFC is allowed a tax credit for income taxes paid by a CFC on certain income attributable to the U.S. shareholder.)</p>"
        },
        "title": "Supply Chain Security and Growth Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1328.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supply Chain Security and Growth Act of 2025</strong></p><p>This bill establishes a tax credit for qualified investments made in certain facilities that are located in a U.S. possession and manufacture drugs, pharmaceuticals, semiconductors, or certain other items, subject to limitations. The bill also increases the deemed-paid foreign tax credit for taxes paid to a U.S. possession.</p><p>Specifically, under the bill, a taxpayer (other than a prohibited foreign entity) is allowed a tax credit for 40% of an investment in certain property that is</p><ul><li>placed into service during the tax year;</li><li>integral to the operation of a critical supply chain facility; and</li><li>constructed, reconstructed, or erected by the taxpayer, or property acquired for original used by the taxpayer.</li></ul><p>The bill defines <em>critical supply chain facility</em> as a facility that (1) manufactures active pharmaceutical ingredients, drugs, biologic products, medical countermeasures, medical diagnostic devices, semiconductors, semiconductor manufacturing equipment, aerospace equipment, or artificial nanomaterials; and (2) is located in Puerto Rico, Guam, American Samoa, the Northern Mariana Islands, or the Virgin Islands.</p><p>Under the bill, the tax credit is transferable and may be claimed as a direct cash payment (i.e., elective payment). (Limitations apply.)</p><p>Finally, the bill increases to 100% (from 80%) the deemed-paid foreign tax credit for income taxes paid or accrued by a controlled foreign corporation (CFC) to a U.S. possession. (Under current law, a U.S. shareholder of a CFC is allowed a tax credit for income taxes paid by a CFC on certain income attributable to the U.S. shareholder.)</p>",
      "updateDate": "2026-05-01",
      "versionCode": "id119hr1328"
    },
    "title": "Supply Chain Security and Growth Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supply Chain Security and Growth Act of 2025</strong></p><p>This bill establishes a tax credit for qualified investments made in certain facilities that are located in a U.S. possession and manufacture drugs, pharmaceuticals, semiconductors, or certain other items, subject to limitations. The bill also increases the deemed-paid foreign tax credit for taxes paid to a U.S. possession.</p><p>Specifically, under the bill, a taxpayer (other than a prohibited foreign entity) is allowed a tax credit for 40% of an investment in certain property that is</p><ul><li>placed into service during the tax year;</li><li>integral to the operation of a critical supply chain facility; and</li><li>constructed, reconstructed, or erected by the taxpayer, or property acquired for original used by the taxpayer.</li></ul><p>The bill defines <em>critical supply chain facility</em> as a facility that (1) manufactures active pharmaceutical ingredients, drugs, biologic products, medical countermeasures, medical diagnostic devices, semiconductors, semiconductor manufacturing equipment, aerospace equipment, or artificial nanomaterials; and (2) is located in Puerto Rico, Guam, American Samoa, the Northern Mariana Islands, or the Virgin Islands.</p><p>Under the bill, the tax credit is transferable and may be claimed as a direct cash payment (i.e., elective payment). (Limitations apply.)</p><p>Finally, the bill increases to 100% (from 80%) the deemed-paid foreign tax credit for income taxes paid or accrued by a controlled foreign corporation (CFC) to a U.S. possession. (Under current law, a U.S. shareholder of a CFC is allowed a tax credit for income taxes paid by a CFC on certain income attributable to the U.S. shareholder.)</p>",
      "updateDate": "2026-05-01",
      "versionCode": "id119hr1328"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1328ih.xml"
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
      "title": "Supply Chain Security and Growth Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T13:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supply Chain Security and Growth Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish the critical supply chains reshoring investment tax credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:19:15Z"
    }
  ]
}
```
