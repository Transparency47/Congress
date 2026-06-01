# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1713?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1713
- Title: Agriculture Innovation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1713
- Origin chamber: Senate
- Introduced date: 2025-05-12
- Update date: 2025-06-05T14:12:54Z
- Update date including text: 2025-06-05T14:12:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-12: Introduced in Senate
- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-05-12: Introduced in Senate

## Actions

- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-12",
    "latestAction": {
      "actionDate": "2025-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1713",
    "number": "1713",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Agriculture Innovation Act of 2025",
    "type": "S",
    "updateDate": "2025-06-05T14:12:54Z",
    "updateDateIncludingText": "2025-06-05T14:12:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-12",
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
          "date": "2025-05-12T21:30:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "SD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1713is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1713\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2025 Ms. Klobuchar (for herself and Mr. Thune ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food Security Act of 1985 to authorize the Secretary of Agriculture to improve agricultural productivity, profitability, resilience, and ecological outcomes through modernized data infrastructure and analysis, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Agriculture Innovation Act of 2025 .\n#### 2. Data on conservation and other production practices\nSubtitle E of title XII of the Food Security Act of 1985 ( 16 U.S.C. 3841 et seq. ) is amended by adding at the end the following:\n1248. Data on conservation and other production practices (a) Purpose The purpose of this section is to improve conservation outcomes, increase agricultural productivity and resilience, and accelerate the development of ecosystem service markets by collecting, analyzing, and providing data\u2014 (1) to better understand how covered conservation practices and suites of covered conservation practices and other production practices impact farm, ranch, and other working land productivity and profitability (such as crop yields, soil health, and other risk-reducing factors); (2) to support the measurement and quantification of ecosystem services provided by working land, such as soil health, water filtration, and habitat, that result from covered conservation practices and other production practices; and (3) to improve the implementation of Department programs to optimize productivity, profitability, and ecological benefits. (b) Definitions In this section: (1) Covered conservation practice The term covered conservation practice means a specific conservation practice or enhancement that is designed to protect soil health, farm and ranch productivity, or both (including the protection of wildlife habitat) while maintaining or enhancing crop yields in an economically sustainable manner (including such a conservation practice or enhancement that is supported by the Department or used independently by a producer), as determined by the Secretary. (2) Department The term Department means the Department of Agriculture. (3) Other production practice The term other production practice means a practice used to produce a crop or livestock, including pest control, nutrient management, manure management, water and irrigation management, seed, feed and nutrition, and crop residue management. (c) Data collection, review, analysis, and technical assistance The Secretary, acting through the 1 or more applicable Under Secretaries that head mission areas relating to farm and ranch productivity and conservation, in coordination with the Chief Data Officer of the Department, the Chief Economist, and the Under Secretary for Research, Education, and Economics, shall carry out the following activities: (1) Identify in the data inventory maintained by the Secretary under section 3511 of title 44, United States Code, data relating to the impacts of covered conservation practices and other production practices on enhancing crop yields, soil health, and ecosystem services, reducing risk, and improving farm, ranch, and other working land profitability generated or collected by the Department, including the Farm Service Agency, the Risk Management Agency, the Natural Resources Conservation Service, the National Agricultural Statistics Service, the Economic Research Service, the Forest Service, and any other relevant agency, as determined by the Secretary. (2) Collect or acquire, using other authorities of the Secretary, and using technology and a modernized survey system, to the greatest extent practicable, or another appropriate method, any additional producer data, baseline data, or other data relating to the impacts of covered conservation practices and other production practices on enhancing crop yields, soil health, and ecosystem services, reducing risk, and improving farm, ranch, and other working land profitability necessary to achieve the purpose described in subsection (a), ensuring that data is collected from all types and sizes of operations. (3) Ensure that producer data identified or collected under paragraph (1) or (2) are collected in a compatible format that is machine-readable (as defined in section 3502 of title 44, United States Code) at the field- and farm-level and in a manner that places the lowest practicable burden on producers and improves the interoperability of the data collected by the Department for the purposes of this section and optimizes the interoperability, to the extent practicable, with data relating to conservation practices generated by other organizations and other activities of the Department. (4) Establish procedures for producers to voluntarily provide supplemental data that may be useful in statistical activities (as defined in section 311 of title 5, United States Code) and activities to build evidence (as defined in that section) of the impacts of covered conservation practices on\u2014 (A) enhancing crop yields, soil health, and ecosystem services; (B) reducing risk; and (C) improving farm, ranch, and other working land profitability. (5) Integrate, collate, and link, to the greatest extent practicable, data identified or collected under this subsection with other government or nongovernmental data sources that include crop yields, soil health, covered conservation practices, and other production practices. (6) Establish a conservation and farm productivity secure data center designed to carry out the purposes of this section that ensures the security, privacy, and integrity of data. (7) Make available data through the secure data center established under paragraph (6) to academic institutions and researchers that meet the user permission requirements described in subsection (d)(2)(A) for the provision of technical assistance. (8) Analyze, consistent with the scientific integrity policy of the Department, the data identified or collected under this subsection to consider the impacts of covered conservation practices and other production practices on enhancing crop yields, soil health, and ecosystem services and improving farm, ranch, and other working land profitability. (9) Use the results of the analyses under paragraph (8) to improve the implementation and efficiency of Department programs to increase productivity, profitability, and ecological benefits of farm, ranch, and other working land, including relating to issues identified in the evidence-building plan of the Department required under section 312 of title 5, United States Code. (10) Promptly make available on the public-facing component of the secure data center established under paragraph (6) the research, analysis, evaluation products, and other information generated in carrying out this section (including open Government data assets (as defined in section 3502 of title 44, United States Code), to the extent permissible by law)\u2014 (A) that demonstrates the impacts of covered conservation practices and other production practices on enhancing crop yields, soil health, and ecosystem services, reducing risk, and improving farm, ranch, and other working land profitability; and (B) in a manner that is easily accessed by producers, researchers, and other stakeholders. (d) Secure agricultural data center establishment (1) In general The Secretary may enter into 1 or more agreements with 1 or more academic institutions, organizations, government agencies, or other experts determined necessary by the Secretary to provide technical assistance, expertise, and technology infrastructure, as needed, to develop the secure data center under subsection (c)(6). (2) Requirement to modernize data security, storage, and access (A) In general In establishing the secure data center described in paragraph (1), the Secretary shall use industry-standard data security protocols and user permissions to protect the security and confidentiality of proprietary producer data while automating and standardizing data collection, storage, and sharing, to the greatest extent practicable, for the purpose of carrying out this section and encouraging agriculture innovation. (B) Requirements In carrying out subparagraph (A), the Secretary shall establish procedures for the operation and use of the secure data center that include\u2014 (i) prohibiting the sale of any individual or identifiable producer data; (ii) a method to provide disclosure review of research resulting from data for which access is provided prior to public release to ensure that no information that is otherwise protected from disclosure by law is disclosed; (iii) requiring any published research to release only aggregated and anonymized data, consistent with best practices for disclosure avoidance and reducing the risk of re-identification; and (iv) periodically consulting with experts and stakeholders to consider necessary modifications to security protocols or confidentiality protections for identifiable data accessed or maintained by the secure data center and improvements to access for approved users. (C) Additional requirements In carrying out subparagraphs (A) and (B), the Secretary shall establish measures to ensure proposals to use data made available through the secure data center to academic institutions and researchers\u2014 (i) would have statistical results that pose no risk of unauthorized disclosure of protected data; (ii) are feasible given the features of the data; and (iii) would be consistent with the purposes for which the data were collected, including for developing evidence that can be used for technical assistance and assessment of program outcomes. (e) Producer tools (1) In general Not later than 3 years after the date of enactment of this section, the Secretary shall provide technical assistance, including through internet-based tools, based on the analysis conducted in carrying out this section and other sources of relevant data, to assist producers in improving sustainable production practices that increase yields and enhance environmental outcomes. (2) Internet-based tools Internet-based tools described in paragraph (1) shall provide to producers, to the greatest extent practicable\u2014 (A) confidential data specific to each farm or ranch of the producer; and (B) general data relating to the impacts of covered conservation practices on enhancing crop yields, soil health, and otherwise reducing risk and improving farm and ranch profitability. (f) Effect on privacy protection laws Nothing in this section affects the applicability to this section of\u2014 (1) section 1770; (2) section 1619 of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 8791 ); (3) section 502(c) of the Federal Crop Insurance Act ( 7 U.S.C. 1502(c) ); (4) section 552a of title 5, United States Code; or (5) any other applicable privacy law that protects personally identifiable information of producers. (g) Reporting Not later than 1 year after the date of enactment of this section, and each year thereafter, the Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report that includes\u2014 (1) a summary of the analysis conducted under this section; (2) the number and regions of producers that voluntarily provided data under subsection (c)(4); (3) a description of any additional or new activities planned to be conducted under this section in the next fiscal year, including\u2014 (A) research relating to any additional conservation practices; (B) any new types of data to be collected; (C) any improved or streamlined data collection efforts associated with this section; and (D) any new research projects; (4) a summary of the procedures for the operation and use of the secure data center under subsection (c)(6), including procedures for protecting the security and confidentiality of proprietary producer data; and (5) in the case of the first 2 reports submitted under this subsection, a description of the current status of the implementation of activities under subsection (c). (h) Funding and administration The Secretary shall use the existing funds and authorities of the Department to carry out this section. (i) Effect Nothing in this section authorizes the Secretary to compel a producer\u2014 (1) to provide data to the Department; or (2) to receive technical assistance. .",
      "versionDate": "2025-05-12",
      "versionType": "Introduced in Senate"
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
        "name": "Agriculture and Food",
        "updateDate": "2025-06-05T14:12:54Z"
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
      "date": "2025-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1713is.xml"
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
      "title": "Agriculture Innovation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Agriculture Innovation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food Security Act of 1985 to authorize the Secretary of Agriculture to improve agricultural productivity, profitability, resilience, and ecological outcomes through modernized data infrastructure and analysis, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:19Z"
    }
  ]
}
```
