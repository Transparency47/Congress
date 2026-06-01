# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7513?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7513
- Title: GSIB Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7513
- Origin chamber: House
- Introduced date: 2026-02-11
- Update date: 2026-02-27T14:32:31Z
- Update date including text: 2026-02-27T14:32:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-02-11: Introduced in House

## Actions

- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7513",
    "number": "7513",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "P000617",
        "district": "7",
        "firstName": "Ayanna",
        "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
        "lastName": "Pressley",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "GSIB Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-27T14:32:31Z",
    "updateDateIncludingText": "2026-02-27T14:32:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-11",
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
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T16:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7513ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7513\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2026 Ms. Pressley (for herself, Mr. Green of Texas , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the global systemically important bank holding companies to provide annual reports to the Board of Governors of the Federal Reserve System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Greater Supervision In Banking Act of 2026 or the GSIB Act of 2026 .\n#### 2. GSIB annual reports\nThe Bank Holding Company Act of 1956 ( 12 U.S.C. 1841 et seq. ) is amended by adding at the end the following:\n15. GSIB annual reports (a) Annual report Each global systemically important bank holding company shall issue an annual report to the Board containing a description of the activities of the company during the previous year and a description of the company\u2019s objectives and goals for the following year. (b) Specific contents Each report required under subsection (a) shall include a description of\u2014 (1) the company\u2019s size and complexity, including a listing of all company subsidiaries and their relationship to specified company business lines; (2) with respect to each depository institution subsidiary of the company, the number and geographic distribution of the branches of such subsidiary; (3) any enforcement actions, including any consent orders and settlements, against the company (including any affiliate or subsidiary of the company), including enforcement actions related to labor and health and safety law violations (in addition to consumer protection); (4) with respect to each enforcement action described under paragraph (3), the total number of consumers, employees, or investors harmed by the conduct that was the basis for such enforcement action; (5) the number of employees dismissed for misconduct, and whether any such employees were company executives; (6) the company\u2019s capital market activities, including with respect to securities (including underwriting, trading, and securitization) and derivatives, including\u2014 (A) the trading desk structure of the company, identifying each desk and the instruments traded or held at each desk; (B) the average and standard deviation of a metric of inventory, constructed using data on individual trading desk positions, for long securities positions, short securities positions, and derivatives, at each individual trading desk for a quarterly period six months prior to the reporting date; (C) how the company complies with restrictions under section 13 of the Bank Holding Company Act of 1956 (commonly referred to as the Volcker Rule ) at each trading desk, including a general description of the methodology for determining reasonably expected near term customer demand and for designing compensation practices at the desk so as not to create incentives for proprietary trading; (D) the total profit or loss attributed to the company\u2019s trading account, including a breakdown of profit earned on fees, commissions, and spreads, and a description of the source of trading account profit or loss that cannot be attributed to fees, commissions, and spreads; and (E) a description of shareholder rights in the jurisdiction of incorporation and in relevant charter and bylaw provisions, including the\u2014 (i) ability and any restrictions to bring shareholder derivative claims, file shareholder proposals, and make books and records requests; (ii) scrutiny conflicted transactions face and any cleansing mechanisms; (iii) standards for determining whether directors are independent and whether large shareholders are controlling shareholders; and (iv) ability to have shareholder contracts that bestow governance rights and any such existing contracts; (7) the extent to which the company utilizes forced arbitration clauses in contracts with consumers, employees, investors, and contractors; (8) the company\u2019s compensation and clawback policies, including\u2014 (A) how these policies are designed to promote accountability of company executives; (B) how the compensation of the chief executive officer and other senior executives compares to the median compensation of an employee of the company; and (C) a detailed description of any stipulation that third-party vendor of the company pays its employees a minimum wage; (9) with respect to compensation paid by the company\u2014 (A) the average amount of compensation received by each decile of employees; (B) a break down of the base pay and incentive pay for each decile, including a description of metrics, sales goals, or cross selling required to be met in order to qualify for the incentive or bonus pay; (C) the minimum wage received by employees; and (D) the number of employees who receive the minimum wage; (10) the diversity of the directors of the company\u2019s board and senior executives, the policies and practices implemented at the company to promote diversity and inclusion among the company\u2019s workforce, and the policies implemented by the company to promote the use of diverse contractors, including diverse asset managers, brokers, and underwriters; (11) the company\u2019s approach to cybersecurity and protecting consumer data; (12) the total number of whistleblower and ethics complaints made by employees through internal company protocols over the past year, what issues were involved in the complaints, and what the resolutions of the complaints were; (13) the company\u2019s actions taken in relation to climate risk and contribution to climate change, including\u2014 (A) any financed emissions targets set by the company and whether they are aligned with global efforts to hold global warming as close to 1.5 degrees Celsius as possible; (B) their reliance on offsets to achieve those targets and the expected sources of those offsets; (C) amount of financing provided in the last year and committed to in future years to companies involved in fossil fuel expansion and any plans to phase out financing to companies involved in fossil fuel expansion; and (D) the projected effect of global failure to achieve the science-based emissions targets on the company\u2019s solvency, operations, and strategy, including the projected effect of 3 degrees Celsius or more of warming; (14) the company\u2019s involvement in projects that contribute to or mitigate disproportionate environmental harms to communities of color or indigenous peoples, or other forms of environmental racism, including\u2014 (A) bank activities, including financing, facilitation, and investment in oil and gas extraction, oil and gas refineries, petrochemical plants and pipeline projects located in low-income census tracts, majority-minority census tracts, or on indigenous lands, or for companies that build or operate these projects; (B) financing for deforestation and mining on indigenous lands anywhere in the world; (C) impact on indigenous people\u2019s rights of any nature-based offsets purchased by the company; and (D) any investments made or other actions taken by the company to address and mitigate previous financing of environmental racism, including but not limited to efforts made to secure Free Prior and Informed Consent; efforts made to compensate impacted individuals living in close proximity to financed oil and gas facilities or projects; and funds for site cleanup; (15) the company\u2019s investments in, partnerships with, and support provided to minority depository institutions and community development financial institutions; (16) the company\u2019s bank activities, including financing, facilitation and investments in, and use of artificial intelligence, including\u2014 (A) analysis of benefits and risks posed to consumers, shareholders, climate, the company\u2019s employees and the markets, generally, by such investments and use; and (B) how any such risks are identified and mitigated by the company, including predeployment testing, transparency reports, red teaming, or security stress testing; (17) any merger or acquisition that was completed in the previous year, including\u2014 (A) a description of how each merger or acquisition affected the company\u2019s size and complexity; (B) an account of the retail branch closures that resulted from the merger or acquisition; (C) a description of any regional markets that experienced a change in market concentration, as measured by the Herfindahl-Hirschman Index, resulting from the merger or acquisition; (D) a description of any regional markets that experienced a change in the company\u2019s regional share of deposits resulting from the merger or acquisition; (E) a list of Federal or State government agencies that approved the transaction; and (F) a description of any conditions placed by a Federal or State government agency on the company when the transaction was approved; and (18) a comparison of how the company\u2019s responses to paragraphs (1) through (16) have changed over the last 10 years. (c) Public availability of reports The Board shall make the reports received under this section available to the public, including on the website of the Board. (d) Global systemically important bank holding company defined In this section, the term global systemically important bank holding company means a global systemically important bank holding company, as such term is defined under section 217.402 of title 12, Code of Federal Regulations. .",
      "versionDate": "2026-02-11",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-02-27T14:32:31Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7513ih.xml"
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
      "title": "GSIB Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-23T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GSIB Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Greater Supervision In Banking Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the global systemically important bank holding companies to provide annual reports to the Board of Governors of the Federal Reserve System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-23T13:18:29Z"
    }
  ]
}
```
