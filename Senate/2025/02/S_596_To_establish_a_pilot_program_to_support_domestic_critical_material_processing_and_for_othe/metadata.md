# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/596?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/596
- Title: Critical Materials Future Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 596
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2026-04-08T16:43:56Z
- Update date including text: 2026-04-08T16:43:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-03-12 - Committee: Committee on Energy and Natural Resources. Hearings held. Hearings printed: S.Hrg. 119-46.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-03-12 - Committee: Committee on Energy and Natural Resources. Hearings held. Hearings printed: S.Hrg. 119-46.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/596",
    "number": "596",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Critical Materials Future Act of 2025",
    "type": "S",
    "updateDate": "2026-04-08T16:43:56Z",
    "updateDateIncludingText": "2026-04-08T16:43:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Hearings held. Hearings printed: S.Hrg. 119-46.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
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
            "date": "2025-03-12T15:58:41Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-12T15:58:41Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-13T20:23:01Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "SC"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "DE"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s596is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 596\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Hickenlooper (for himself, Mr. Graham , Mr. Coons , and Mr. Young ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo establish a pilot program to support domestic critical material processing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Critical Materials Future Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Country of risk**\nThe term country of risk has the meaning given the term in section 10114(a) of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 18912(a) ).\n**(2) Critical material**\nThe term critical material has the meaning given the term in section 7002(a) of the Energy Act of 2020 ( 30 U.S.C. 1606(a) ).\n**(3) Domestic**\nThe term domestic means facilities operating within the United States or within any territory or possession of the United States.\n**(4) Eligible project**\nThe term eligible project means a project that refines and processes or recycles raw critical materials into purified forms suitable for first-use applications.\n**(5) Entity of concern**\n**(A) In general**\nThe term entity of concern has the meaning given the term in section 10114(a) of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 18912(a) ); and\n**(B) Inclusion**\nThe term entity of concern includes an entity that the Secretary has determined, using a risk-based approach, is subject to the control or influence of a foreign nation whose strategic interests concerning critical materials does not align with the strategic interests of the United States.\n**(6) Innovative financial tools**\nThe term innovative financial tools means financial instruments to support demand-side economic mechanisms, including\u2014\n**(A)**\npricing support mechanisms, such as contracts for difference and price floors, advanced market commitments, and forward contracts; and\n**(B)**\nother transactions that the Secretary may enter into under section 646 of the Department of Energy Organization Act ( 42 U.S.C. 7256 ).\n**(7) Pilot program**\nThe term Pilot Program means the Domestic Critical Material Processing Pilot Program established under section 4(a).\n**(8) Reliable sources**\n**(A) In general**\nThe term reliable source has the meaning given the term in section 12 of the Strategic and Critical Materials Stock Piling Act ( 50 U.S.C. 98h\u20133 ).\n**(B) Inclusions**\nThe term reliable source includes facilities owned by, controlled by, or subject to the jurisdiction of any country\u2014\n**(i)**\nwith which the United States has a free trade agreement in effect; and\n**(ii)**\ndesignated a major non-NATO ally under section 517 of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2321k ).\n**(9) Secretary**\nThe term Secretary means the Secretary of Energy.\n#### 3. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto support domestic critical material processing with innovative financial tools to reduce supply chain vulnerabilities and enhance energy and national security; and\n**(2)**\nto evaluate the effectiveness of innovative financial tools in supporting investment in and expanding domestic critical materials processing, including the impact of different support mechanisms on project development for various critical materials and fostering more liquid, transparent, and predictable markets for critical materials.\n#### 4. Domestic critical material processing pilot program\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a pilot program, to be known as the Domestic Critical Material Processing Pilot Program , to support not fewer than 3 domestic critical material processing projects.\n##### (b) Objectives\nThe objectives of the Pilot Program are\u2014\n**(1)**\nto provide financial stability and attract private investment in eligible domestic critical material processing projects;\n**(2)**\nto analyze how different financial tools influence critical material market dynamics and projects and the estimated level of financial support needed to secure reliable United States supply chains for various critical materials and support a sufficient domestic critical materials processing industry; and\n**(3)**\nto reduce supply chain vulnerabilities and enhance energy security and national security.\n##### (c) Requirements\n**(1) Implementation**\n**(A) Regulations**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall issue regulations to implement the Pilot Program.\n**(B) Other transaction authority**\nIn carrying out the Pilot Program, the Secretary shall have the authority to enter into other transactions in the same manner and subject to the same terms and conditions as transactions that the Secretary may enter into under section 646 of the Department of Energy Organization Act ( 42 U.S.C. 7256 ).\n**(C) Flexible hiring authority**\nThe Secretary may appoint and fix the compensation of such temporary personnel as may be necessary to carry out and implement the Pilot Program, without regard to the provisions of subchapter I of chapter 33 of title 5, United States Code, governing appointments in competitive service and compensation of personnel.\n**(D) Consultation**\nThe Secretary shall consult outside stakeholders and experts, including mining and critical material processing industry representatives, financial experts, and academic researchers, during development of the Pilot Program for purposes of improving the effectiveness and efficiency of the Pilot Program.\n**(2) Diversity**\n**(A) In general**\nSubject to subparagraph (B), the Pilot Program shall provide support for the processing of not fewer than 3 different critical materials in order to gain insight into the impact of innovative financial tools on different critical material markets.\n**(B) Limitation**\nSupport provided under subparagraph (A) to a single critical material shall not exceed 50 percent of any funding provided to the Pilot Program under subsection (h).\n**(3) Sunset**\nThe Pilot Program shall terminate on the date that is not later than 5 years after the date the Pilot Program is established under subsection (a).\n##### (d) Applications\n**(1) In general**\nApplications under the Pilot Program for eligible projects shall be submitted to the Secretary at such time, in such manner, and containing such information as the Secretary may require.\n**(2) Eligibility criteria**\n**(A) In general**\nThe Secretary shall review and select applications under the Pilot Program for eligible projects based on\u2014\n**(i)**\nthe potential of the eligible project to enhance the economic, energy, and national security of the United States;\n**(ii)**\nthe economic competitiveness of the eligible project;\n**(iii)**\nthe economic and financial sustainability of the eligible project, using information such as\u2014\n**(I)**\nthe potential for the applicant of the eligible project to secure an offtake agreement if the eligible project is selected; and\n**(II)**\nan analysis of the estimated production costs of the eligible project and prevailing or anticipated market prices;\n**(iv)**\nthe potential of the eligible project to mitigate risks associated with importing critical materials from entities of concern;\n**(v)**\nthe prioritization requirements described in subparagraph (B); and\n**(vi)**\nother factors, as determined by the Secretary, in coordination with the agencies described in subsection (e).\n**(B) Priority**\nIn selecting applications under the Pilot Program for eligible projects, the Secretary shall prioritize eligible projects\u2014\n**(i)**\nthat use feedstock from domestic or reliable sources, with higher priority given to eligible projects that have greater use of feedstock from domestic sources;\n**(ii)**\nthe selection of which would support the ability of the applicant to secure an offtake agreement with domestic or reliable sources; and\n**(iii)**\nthat are the most economically competitive, as determined by the Secretary, based on factors including\u2014\n**(I)**\nthe potential for the applicant of the eligible project to secure an offtake agreement if selected; and\n**(II)**\nthe difference between the estimated production costs of the eligible project and prevailing or anticipated market prices.\n**(3) Timeline**\nThe Secretary shall select applications under the Pilot Program for eligible projects not later than 1 year after the date of enactment of this Act.\n##### (e) Coordination\n**(1) In general**\nTo ensure the efficient implementation and operation of the Pilot Program, the Secretary shall coordinate with\u2014\n**(A)**\nthe Secretary of Commerce;\n**(B)**\nthe Secretary of Defense;\n**(C)**\nthe Secretary of the Interior;\n**(D)**\nthe Secretary of State;\n**(E)**\nthe Director of the United States Geological Survey;\n**(F)**\nthe United States Trade Representative; and\n**(G)**\nthe heads of other Federal departments and agencies, as determined by the Secretary.\n**(2) Security research and development**\nWhen selecting applications and determining the level of financial support for each project under the Pilot Program, the Secretary shall coordinate with the Secretary of Defense to incorporate insights from the Open Price Exploration for National Security research and development program of the Defense Advanced Research Projects Agency.\n##### (f) Study\n**(1) In general**\nNot later than 2 years after the date on which the Pilot Program terminates under subsection (c)(3), the Secretary shall conduct and publish a study on\u2014\n**(A)**\nthe impact of innovative financial tools on the critical materials sector and the relative cost-effectiveness of those tools in supporting domestic critical materials processing projects and developing more liquid, transparent, and predictable markets for critical materials;\n**(B)**\nthe estimated level of financial support needed to secure reliable United States supply chains for various critical materials and support a sufficient domestic critical materials processing industry;\n**(C)**\nthe potential of critical material recycling to support the domestic critical materials market;\n**(D)**\nthe effectiveness of the Pilot Program, including an evaluation of each eligible project supported by the Pilot Program; and\n**(E)**\nwhether the models of the Open Price Exploration for National Security research and development program of the Defense Advanced Research Projects Agency allowed the Pilot Program to better anticipate market trends, optimize resource allocation, and provide the appropriate level of support based on current and future critical material market needs.\n**(2) Insights**\nThe study under paragraph (1) shall include insights into concerns of private investors in different critical material markets and the impact of innovative financial tools on catalyzing final investment decisions.\n**(3) Stakeholder engagement**\nThe study under paragraph (1) shall be carried out in consultation with relevant stakeholders, as determined by the Secretary, including mining and critical material processing industry representatives, financial experts, local governments hosting critical material processing projects, and academic researchers.\n**(4) DARPA OPEN program**\nThe Secretary shall share the results of the study under paragraph (1) with the Open Price Exploration for National Security research and development program of the Defense Advanced Research Projects Agency to inform ongoing research and development of tools to support transparency in domestic critical materials markets.\n##### (g) Report\n**(1) In general**\nThe Secretary shall submit to the Committees on Energy and Natural Resources, Foreign Relations, and Armed Services of the Senate, and the Committees on Natural Resources, Energy and Commerce, and Armed Services of the House of Representatives, an annual report for each year that the Pilot Program is carried out.\n**(2) Contents**\nThe report under paragraph (1) shall include\u2014\n**(A)**\nactivities, expenditures, and outcomes of the Pilot Program;\n**(B)**\nrecommendations to Congress on the continuation or expansion of the Pilot Program; and\n**(C)**\nrecommendations for how the Federal Government should use innovative financial tools\u2014\n**(i)**\nto increase domestic critical materials processing capacity;\n**(ii)**\nto strengthen domestic critical material supply chains by increasing United States processing capacity using domestic feedstock;\n**(iii)**\nto mitigate market volatility;\n**(iv)**\nto boost price transparency in critical materials markets;\n**(v)**\nto leverage market indices in countries other than those designated as countries of risk;\n**(vi)**\nto ensure long-term adequate supplies of critical materials for the economy of the United States; and\n**(vii)**\nto increase the domestic recycling of critical materials.\n##### (h) Funding\n**(1) Financial mechanisms**\n**(A) In general**\nIn establishing and carrying out the Pilot Program, the Secretary shall enter into agreements, including contracts, grants, and cooperative agreements, and other transactions, as determined by the Secretary, to enable the use of innovative financial tools to support domestic critical material processing projects.\n**(B) Authority**\nIn carrying out subparagraph (A), the Secretary may use innovative financial tools, including price support such as contracts for differences, and leverage functions to develop and drive critical materials processing to entities that are not entities of concern, under such terms and conditions as the Secretary determines to be necessary or appropriate.\n**(2) Reinvestment of revenue**\n**(A) Establishment**\nThere is established in the Treasury of the United States a fund, to be known as the Critical Materials Revolving Fund (referred to in this paragraph as the Fund ).\n**(B) Purposes**\nThe Fund shall be available to the Secretary as a revolving fund\u2014\n**(i)**\nto reinvest amounts generated from eligible projects into new critical materials processing projects under the Pilot Program; and\n**(ii)**\nto further enhance the objectives of the Pilot Program.\n**(3) Authorization of appropriations**\nThere is authorized to be appropriated to the Secretary to carry out this Act $750,000,000, to remain available until expended.",
      "versionDate": "2025-02-13",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Competitiveness, trade promotion, trade deficits",
            "updateDate": "2025-06-04T15:13:04Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-04T15:13:23Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-06-04T15:12:56Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-06-04T15:13:30Z"
          },
          {
            "name": "Industrial policy and productivity",
            "updateDate": "2025-06-04T15:13:35Z"
          },
          {
            "name": "Strategic materials and reserves",
            "updateDate": "2025-06-04T15:13:14Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-08T16:43:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-06-24T20:27:46Z"
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
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s596is.xml"
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
      "title": "Critical Materials Future Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Critical Materials Future Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T15:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a pilot program to support domestic critical material processing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T15:33:29Z"
    }
  ]
}
```
