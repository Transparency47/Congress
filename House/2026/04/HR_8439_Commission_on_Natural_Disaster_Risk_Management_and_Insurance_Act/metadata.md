# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8439?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8439
- Title: Commission on Natural Disaster Risk Management and Insurance Act
- Congress: 119
- Bill type: HR
- Bill number: 8439
- Origin chamber: House
- Introduced date: 2026-04-22
- Update date: 2026-05-06T16:14:37Z
- Update date including text: 2026-05-06T16:14:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-22 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-22: Introduced in House

## Actions

- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-22 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8439",
    "number": "8439",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001112",
        "district": "24",
        "firstName": "Salud",
        "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
        "lastName": "Carbajal",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Commission on Natural Disaster Risk Management and Insurance Act",
    "type": "HR",
    "updateDate": "2026-05-06T16:14:37Z",
    "updateDateIncludingText": "2026-05-06T16:14:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T15:02:45Z",
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
          "date": "2026-04-22T15:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "CO"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "LA"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8439ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8439\nIN THE HOUSE OF REPRESENTATIVES\nApril 22, 2026 Mr. Carbajal (for himself, Mr. Evans of Colorado , Mr. Carter of Louisiana , and Mr. Ezell ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a nonpartisan commission on natural disaster risk management, insurance, and other financial and economic protections, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Commission on Natural Disaster Risk Management and Insurance Act .\n#### 2. Establishment\nThere is established an independent, nonpartisan Commission on Natural Disaster Risk Management and Insurance (in this Act referred to as the Commission ).\n#### 3. Membership and structure\n##### (a) Appointment\nThe Commission shall be composed of\u2014\n**(1)**\n8 members who shall have general knowledge and expertise in insurance, reinsurance, insurance regulation, policyholder concerns, emergency management, risk management, public finance, financial markets, actuarial analysis, flood mapping and planning, structural engineering, building standards, land use planning, natural disasters, meteorology, seismology, environmental issues, quantitative catastrophic risk modeling, or other pertinent qualifications, of which\u2014\n**(A)**\n2 members shall be appointed by the majority leader of the Senate;\n**(B)**\n2 members shall be appointed by the minority leader of the Senate;\n**(C)**\n2 members shall be appointed by the Speaker of the House of Representatives; and\n**(D)**\n2 members shall be appointed by the minority leader of the House of Representatives;\n**(2)**\n8 members who shall have knowledge and expertise in insurance, reinsurance, policyholder concerns, risk management, financial markets, urban development or other pertinent financial services or housing qualifications, of which\u2014\n**(A)**\n2 members shall be appointed by the Chair of the Committee on Banking, Housing, and Urban Affairs of the Senate;\n**(B)**\n2 members shall be appointed by the Ranking Member of the Committee on Banking, Housing, and Urban Affairs of the Senate;\n**(C)**\n2 members shall be appointed by the Chair of the Committee on Financial Services of the House of Representatives; and\n**(D)**\n2 members shall be appointed by the Ranking Member of the Committee on Financial Services of the House of Representatives;\n**(3)**\n8 members who shall have knowledge and expertise in disaster response and preparedness, emergency management, public financing, structural engineering, building standards, and other pertinent government response and investment qualifications, of which\u2014\n**(A)**\n2 members shall be appointed by the Chair of the Committee on Transportation and Infrastructure of the House of Representatives;\n**(B)**\n2 members shall be appointed by the Ranking Member of the Committee on Transportation and Infrastructure of the House of Representatives;\n**(C)**\n2 members shall be appointed by the Chair of the Committee on Homeland Security and Governmental Affairs of the Senate; and\n**(D)**\n2 members shall be appointed by the Ranking Member of the Committee on Homeland Security and Governmental Affairs of the Senate; and\n**(4)**\n2 members who shall be State insurance commissioners, to be appointed by a selection process determined by the State insurance commissioners.\n##### (b) Limitations\nMembers of the Commission appointed under\u2014\n**(1)**\nsubsection (a)(1) through (a)(3) shall not be officers or employees of the United States Government or any State government; and\n**(2)**\nsubsection (a)(4) shall not be from the same political party.\n##### (c) Period of appointment\n**(1) In general**\nEach member of the Commission shall\u2014\n**(A)**\nbe appointed not later than 30 days after the date of the enactment of this Act; and\n**(B)**\nserve for the duration of the Commission.\n**(2) Vacancies**\nA vacancy on the Commission\u2014\n**(A)**\nshall not affect the powers and duties of the Commission; and\n**(B)**\nshall be filled in the same manner as the original appointment.\n##### (d) Basic pay\nMembers of the Commission shall serve without pay.\n##### (e) Quorum\n**(1) Majority**\nA majority of the members of the Commission shall constitute a quorum, but a lesser number, as determined by the Commission, may hold hearings.\n**(2) Approval actions**\nAll recommendations and reports of the Commission required by this Act shall be approved only by a majority vote of all of the members of the Commission.\n##### (f) Chairperson\nThe Commission shall, by majority vote of all of the members of the Commission, select 1 member of the Commission to serve as the Chairperson of the Commission.\n##### (g) Meetings\nThe Commission shall meet at the call of the Chairperson of the Commission or a majority of the members of the Commission.\n##### (h) Information\n**(1) Access**\n**(A) In general**\nThe Commission may enter into information-sharing agreements with Federal, State, local and Tribal government entities related to relevant information, including nonpublicly available data.\n**(B) Limitation**\nThe Commission may not enter into an information sharing-agreement described in subparagraph (A) with respect to information that contains personal identifiable information.\n**(2) Confidentiality**\n**(A) Retention of privilege**\nThe sharing or submission of any nonpublicly available data and information to the Commission shall not constitute a waiver of, or otherwise affect, any privilege arising under Federal or State law (including the rules of any Federal or State court) to which the data or information is otherwise subject.\n**(B) Continued application of prior confidentiality agreements**\nAny requirement under Federal or State law to the extent otherwise applicable, or any requirement pursuant to a written agreement in effect between the original source of any nonpublicly available data or information and the source of such data or information to the Commission, regarding the privacy or confidentiality of any data or information in the possession of the source to the Commission, shall continue to apply to such data or information after the data or information has been provided to the Commission.\n**(3) Limitation**\nNothing in this Act shall be construed to\u2014\n**(A)**\nrequire any Federal, State, local or Tribal government agency to share data or information to the Commission;\n**(B)**\nauthorize the Commission to require data or information from any stakeholder; or\n**(C)**\nallow any Federal, State, local or Tribal government to collect information for which they do not already have for the sole purpose of the work of the Commission.\n##### (i) Gifts\nThe Commission may not receive gifts to assist it in carrying out its duties without a specific authorization.\n#### 4. Duties of the commission\n##### (a) Assessment\nThe Commission shall examine the risks posed to the United States (both nationally and to individual States, localities, tribes and other geographic areas) by natural disasters and means for mitigating the risks and financial costs associated with losses caused by natural disasters, including the assessment of\u2014\n**(1)**\nthe current exposure of the United States to natural disasters, including wildfires, hurricanes, earthquakes, volcanic eruptions, tsunamis, severe storms (including tornados, hail, and damaging winds), extreme heat, winter storms, flooding, droughts, and other natural disasters;\n**(2)**\ndemographic trends, including population migration to high-risk areas and the associated development of the built environment, and the impact such trends could have on the cost of losses inflicted by future natural disasters;\n**(3)**\nthe current efforts of States, communities, and individuals to mitigate their natural disaster risks, including the affordability and effectiveness of such mitigation;\n**(4)**\nthe impact and benefits of strengthened land use regulations and building codes in areas at high risk for natural disasters, and methods to strengthen enforcement of structural mitigation and vulnerability reduction measures, such as zoning and building code compliance;\n**(5)**\nthe role of Federal, State, and local governments in providing incentives for feasible risk mitigation efforts;\n**(6)**\nthe current condition of, as well as the outlook for, the availability and affordability of property and casualty insurance in all regions of the country and an analysis of factors that may be adversely impacting such availability and affordability;\n**(7)**\nthe impact of Federal and State laws, regulations, and policies (including rate regulation, market access requirements, reinsurance, accounting and tax policies, State residual markets, and State disaster funds) on\u2014\n**(A)**\nthe affordability and availability of insurance for losses resulting from natural disaster;\n**(B)**\nthe capacity of the private insurance market to cover losses resulting from natural disasters;\n**(C)**\nthe commercial and residential development of high-risk areas; and\n**(D)**\nthe costs of natural disasters to Federal and State taxpayers;\n**(8)**\nthe present and long-term financial condition of State residual markets and natural disaster funds in high-risk regions, including the likelihood of insolvency following a natural disaster, the concentration of risks within such funds, the reliance on post-event assessments and State funding, and the adequacy of rates;\n**(9)**\nthe various risk-sharing mechanisms for natural disasters (including the private insurance and reinsurance markets, State residual insurance markets, catastrophe bond markets, and government insurance programs) and the relevant benefits, risks and practices for providing insurance protection to different sectors of the population of the United States;\n**(10)**\nthe role that innovation in financial services could play in improving the financial risk-sharing of the costs of natural disasters, specifically addressing measures that could foster the development of financial products designed to cover natural disaster risk, such as alternative risk transfer mechanisms, including parametric insurance and catastrophe bonds;\n**(11)**\nwhether, and how, such risk-sharing mechanisms can be modified to resolve key obstacles currently impeding broader take-up rate of catastrophic risk management and financing;\n**(12)**\nthe ability of the United States private insurance market to cover insured losses caused by natural disasters, including an estimate of the maximum amount of insured losses that could be sustained during a single year and the probability of natural disasters occurring in a single year that would inflict more insured losses than the United States insurance and reinsurance markets could sustain;\n**(13)**\nthe need for financial feasibility and sustainability of a national, regional, or other cooperation designed to promote adequate property and casualty insurance take-up, including in current impacted or constrained markets;\n**(14)**\nthe appropriate role, if any, for the Federal Government in the stabilization of property and casualty insurance, reinsurance, or other impacted markets following catastrophic loss events;\n**(15)**\nmethods to promote the take-up of flood insurance policies through the National Flood Insurance Program to reduce financial losses caused by natural disasters in the uninsured sectors of the population of the United States; and\n**(16)**\nany unique needs of low-income communities to promote risk reduction and property and casualty insurance take-up in such communities.\n##### (b) Consultation and public engagement\nIn conducting the assessments required in subsection (a), the Commission shall\u2014\n**(1)**\ncoordinate with State insurance commissioners, both individually and collectively, on all insurance matters;\n**(2)**\nconsult with relevant Federal agencies, as described in subsection (c), on matters related to the prevalence and cost of Federal financial assistance related to losses resulting from natural disasters; and\n**(3)**\nengage with relevant public stakeholders, including\u2014\n**(A)**\ninsurers, reinsurers, and insurance agents and brokers; and\n**(B)**\ncapital market participants with a focus on alternative risk transfer mechanisms.\n##### (c) Executive branch assistance\nThe heads of the following agencies shall advise and consult with the Commission on matters within their respective areas of responsibility:\n**(1)**\nFederal Emergency Management Agency.\n**(2)**\nU.S. Army Corps of Engineers.\n**(3)**\nNational Oceanic and Atmospheric Administration.\n**(4)**\nDepartment of Housing and Urban Development.\n**(5)**\nDepartment of Housing and Urban Development.\n**(6)**\nFederal Housing Finance Agency.\n**(7)**\nFederal Housing Administration.\n**(8)**\nDepartment of the Treasury.\n**(9)**\nDepartment of Agriculture.\n**(10)**\nEnvironmental Protection Agency.\n**(11)**\nAny other agency, as determined by the Commission.\n#### 5. Report\nNot later than 2 years after the date of the enactment of this Act, the Commission shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate, the Committee on Financial Services of the House of Representatives, Committee on Homeland Security and Governmental Affairs of the Senate, and the Committee on Transportation and Infrastructure of the House of Representatives a report that contains\u2014\n**(1)**\na detailed statement of the findings and assessments conducted by the Commission pursuant to section 4; and\n**(2)**\nany recommendations for legislative, regulatory, administrative, or other actions at the Federal, State, or local levels that the Commission considers appropriate to address the issues described in section 4.\n#### 6. Termination\n##### (a) In general\nThe Commission shall terminate 90 days after the date on which the Commission submits the report under section 5.\n##### (b) Data and information\nUpon the termination of the Commission, all data and information in possession of the Commission and its members shall be destroyed or returned to the respective owners of such data and information.\n#### 7. Authorization of appropriations\nThere are authorized to be appropriated to the Commission such sums as may be necessary to carry out this Act, to remain available until expended.",
      "versionDate": "2026-04-22",
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
        "updateDate": "2026-05-06T16:14:36Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8439ih.xml"
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
      "title": "Commission on Natural Disaster Risk Management and Insurance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T05:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Commission on Natural Disaster Risk Management and Insurance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a nonpartisan commission on natural disaster risk management, insurance, and other financial and economic protections, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-28T05:48:31Z"
    }
  ]
}
```
