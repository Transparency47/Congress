# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/422?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/422
- Title: No Subsidies for Wealthy Universities Act
- Congress: 119
- Bill type: HR
- Bill number: 422
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-15 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-15 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/422",
    "number": "422",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "No Subsidies for Wealthy Universities Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-15T15:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "GA"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "MD"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr422ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 422\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Cline (for himself, Mr. Clyde , and Mr. Harris of Maryland ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish Federal research award reimbursement limits for indirect costs for institutions of higher education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Subsidies for Wealthy Universities Act .\n#### 2. Definitions\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given the term in section 551 of title 5, United States Code.\n**(2) Direct cost**\nThe term direct cost has the meaning given the term in subpart E of part 200 of title 2, Code of Federal Regulations (or any successor regulation).\n**(3) Endowment fund**\nThe term endowment fund has the meaning given the term in section 312(c) of the Higher Education Act of 1965 ( 20 U.S.C. 1058(c) ).\n**(4) Federal research award**\nThe term Federal research award means support provided to an individual or entity by an agency to carry out research activities, which may include support in the form of a grant, contract, cooperative agreement, or other transaction.\n**(5) Indirect cost**\nThe term indirect cost has the meaning given the term in subpart E of part 200 of title 2, Code of Federal Regulations (or any successor regulation).\n**(6) Indirect cost rate**\nThe term indirect cost rate , with respect to a project supported under a Federal research award, means the ratio, expressed as a percentage, of the indirect costs of the project to the direct costs of the project, as determined in accordance with subpart E of part 200 of title 2, Code of Federal Regulations (or any successor regulation).\n**(7) Institution of higher education**\nThe term institution of higher education has the meaning given such term in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 ).\n#### 3. Capping indirect costs allowable under Federal research awards\n##### (a) Endowment calculations\n**(1) Collection by NCES**\nNot later than September 30 of each year, the Commissioner for Education Statistics shall\u2014\n**(A)**\ncollect information regarding the value of the endowment funds, as of September 30 of the preceding fiscal year, of each institution of higher education that has entered into a program participation agreement with the Secretary of Education under section 487(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a) );\n**(B)**\nuse the data described in subparagraph (A) to identify\u2014\n**(i)**\neach such institution of higher education with endowment funds that, in total, are valued at more than $5,000,000,000, as of September 30 of the preceding fiscal year; and\n**(ii)**\neach such institution of higher education with endowments funds that, in total, are valued at more than $2,000,000,000 but not more than $5,000,000,000, as of September 30 of the preceding fiscal year; and\n**(C)**\nmake lists of the institutions identified under each of clauses (i) and (ii) of subparagraph (B) and submit such lists to the Director of the Office of Management and Budget.\n**(2) Distribution by OMB**\nNot later than September 30 of each year, the Director of the Office of Management and Budget shall make the lists described in paragraph (1)(C) available to\u2014\n**(A)**\nthe head of each agency;\n**(B)**\nCongress; and\n**(C)**\nthe public.\n##### (b) Limits on indirect cost reimbursements for institutions with significant endowment funds\n**(1) Prohibition for institutions with highest endowment funds**\nNotwithstanding any other provision of law, the head of an agency making a Federal research award for a fiscal year to an institution of higher education identified under subsection (a)(1)(B)(i) for the preceding fiscal year shall not allow any Federal research award funds to be used for indirect costs.\n**(2) Indirect cost rate limit for institutions with substantial endowment funds**\nNotwithstanding any other provision of law, the head of an agency making a Federal research award for a fiscal year to an institution of higher education identified under subsection (a)(1)(B)(ii) for the preceding fiscal year shall establish an indirect cost rate for the Federal research award that is not more than 8 percent.\n##### (c) Limits on indirect cost reimbursements rates for other institutions\nNotwithstanding any other provision of law, the head of an agency making a Federal research award for a fiscal year to an institution of higher education not identified under clause (i) or (ii) of subsection (a)(1)(B) for the preceding fiscal year shall establish an indirect cost rate for the Federal research award that is not more than 15 percent.\n##### (d) Program participation agreement requirement\nSection 487(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a) ) is amended by adding at the end the following:\n(30) The institution will annually provide the Commissioner for Education Statistics with the endowment fund information needed by the Commissioner to carry out section 3(a)(1) of the No Subsidies for Wealthy Universities Act . .\n#### 4. Improving oversight of indirect cost reimbursement\nThe Comptroller General of the United States shall prepare and submit to Congress an annual report regarding the indirect costs reimbursed under Federal research awards made to institutions of higher education for the preceding fiscal year. The report shall\u2014\n**(1)**\ndetermine, to the extent practicable, for such fiscal year\u2014\n**(A)**\nthe amount of reimbursed indirect costs for Federal research awards that were used for administrative staff compensation at institutions of higher education; and\n**(B)**\nthe amount of reimbursed indirect costs for Federal research awards that were used for compensation for administrative staff members with responsibilities related to diversity, equity, and inclusion;\n**(2)**\nidentify the research fields that receive the highest levels of funding from Federal research awards made to institutions of higher education; and\n**(3)**\nidentify\u2014\n**(A)**\nthe agencies that awarded the highest amount of Federal research award funds to institutions of higher education; and\n**(B)**\nthe institutions of higher education that received Federal research awards from such agencies.\n#### 5. Effective date; applicability\nThis Act shall take effect on the date that is 1 year after the date of enactment on this Act and shall apply with respect to Federal research awards made on or after such date.",
      "versionDate": "2025-01-15",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-12T13:41:23Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-12T13:41:15Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-03-12T13:41:00Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-03-12T13:41:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-02-13T21:49:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr422",
          "measure-number": "422",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr422v00",
            "update-date": "2025-04-02"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Subsidies for Wealthy Universities Act</strong></p><p>This bill limits the indirect costs that are allowable under federal research awards to institutions of higher education (IHEs) with endowments above specified thresholds.\u00a0(Generally, indirect costs represent expenses that are not specific to a research project but are needed to maintain the infrastructure and administrative support for federally funded research.)</p><p>Specifically, the National Center for Education Statistics (NCES) must annually collect information regarding the endowments of each IHE that has entered into a program participation agreement with the Department of Education.</p><p>With this collected information,\u00a0NCES must identify and make lists of (1) each IHE with an endowment of more than $5 billion, and (2) each IHE with an endowment of more than $2 billion (but not more than $5 billion). NCES must submit these lists to the Office of Management and Budget, which must then distribute the lists to federal agencies, Congress, and the public.</p><p>The bill establishes the following limits on the indirect costs allowable under federal research awards:</p><ul><li>for an IHE with an endowment of more than $5 billion,\u00a0the IHE is prohibited from using these awards for indirect costs;</li><li>for an IHE with an endowment of more than $2 billion (but not more than $5 billion),\u00a0the IHE is limited to\u00a0an indirect cost rate of 8%; and</li><li>for all other IHEs, an\u00a0indirect cost rate of 15%.</li></ul><p>The Government Accountability Office must annually report to Congress on indirect cost reimbursement on federal research awards for IHEs.</p>"
        },
        "title": "No Subsidies for Wealthy Universities Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr422.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Subsidies for Wealthy Universities Act</strong></p><p>This bill limits the indirect costs that are allowable under federal research awards to institutions of higher education (IHEs) with endowments above specified thresholds.\u00a0(Generally, indirect costs represent expenses that are not specific to a research project but are needed to maintain the infrastructure and administrative support for federally funded research.)</p><p>Specifically, the National Center for Education Statistics (NCES) must annually collect information regarding the endowments of each IHE that has entered into a program participation agreement with the Department of Education.</p><p>With this collected information,\u00a0NCES must identify and make lists of (1) each IHE with an endowment of more than $5 billion, and (2) each IHE with an endowment of more than $2 billion (but not more than $5 billion). NCES must submit these lists to the Office of Management and Budget, which must then distribute the lists to federal agencies, Congress, and the public.</p><p>The bill establishes the following limits on the indirect costs allowable under federal research awards:</p><ul><li>for an IHE with an endowment of more than $5 billion,\u00a0the IHE is prohibited from using these awards for indirect costs;</li><li>for an IHE with an endowment of more than $2 billion (but not more than $5 billion),\u00a0the IHE is limited to\u00a0an indirect cost rate of 8%; and</li><li>for all other IHEs, an\u00a0indirect cost rate of 15%.</li></ul><p>The Government Accountability Office must annually report to Congress on indirect cost reimbursement on federal research awards for IHEs.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr422"
    },
    "title": "No Subsidies for Wealthy Universities Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Subsidies for Wealthy Universities Act</strong></p><p>This bill limits the indirect costs that are allowable under federal research awards to institutions of higher education (IHEs) with endowments above specified thresholds.\u00a0(Generally, indirect costs represent expenses that are not specific to a research project but are needed to maintain the infrastructure and administrative support for federally funded research.)</p><p>Specifically, the National Center for Education Statistics (NCES) must annually collect information regarding the endowments of each IHE that has entered into a program participation agreement with the Department of Education.</p><p>With this collected information,\u00a0NCES must identify and make lists of (1) each IHE with an endowment of more than $5 billion, and (2) each IHE with an endowment of more than $2 billion (but not more than $5 billion). NCES must submit these lists to the Office of Management and Budget, which must then distribute the lists to federal agencies, Congress, and the public.</p><p>The bill establishes the following limits on the indirect costs allowable under federal research awards:</p><ul><li>for an IHE with an endowment of more than $5 billion,\u00a0the IHE is prohibited from using these awards for indirect costs;</li><li>for an IHE with an endowment of more than $2 billion (but not more than $5 billion),\u00a0the IHE is limited to\u00a0an indirect cost rate of 8%; and</li><li>for all other IHEs, an\u00a0indirect cost rate of 15%.</li></ul><p>The Government Accountability Office must annually report to Congress on indirect cost reimbursement on federal research awards for IHEs.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr422"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr422ih.xml"
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
      "title": "No Subsidies for Wealthy Universities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Subsidies for Wealthy Universities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish Federal research award reimbursement limits for indirect costs for institutions of higher education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T02:48:18Z"
    }
  ]
}
```
