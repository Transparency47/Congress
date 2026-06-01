# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7188?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7188
- Title: MOLD Act
- Congress: 119
- Bill type: HR
- Bill number: 7188
- Origin chamber: House
- Introduced date: 2026-01-21
- Update date: 2026-05-20T08:08:04Z
- Update date including text: 2026-05-20T08:08:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-21: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-01-21: Introduced in House

## Actions

- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-21",
    "latestAction": {
      "actionDate": "2026-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7188",
    "number": "7188",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "MOLD Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:04Z",
    "updateDateIncludingText": "2026-05-20T08:08:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-21",
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
          "date": "2026-01-21T15:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "GU"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "FL"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "SC"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "MA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "NE"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "NY"
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
      "sponsorshipDate": "2026-02-26",
      "state": "VA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-03-30",
      "state": "TX"
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
      "sponsorshipDate": "2026-04-02",
      "state": "PA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "HI"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NC"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NH"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "PA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7188ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7188\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2026 Mr. Panetta (for himself, Mr. Moylan , and Mr. Bilirakis ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo improve housing and environmental health and safety protections for members of the Armed Forces and their families residing in military family housing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Military Occupancy Living Defense Act or the MOLD Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Secretary of Defense should establish and implement a uniform code of basic housing standards for safety, comfort, and habitability for privatized military housing, which meets or exceeds requirements informed by a nationally recognized, consensus-based, model property maintenance code.\n**(2)**\nThousands of military families living in privatized military housing have been exposed to hazardous environmental conditions, including widespread mold contamination, due to negligent maintenance practices and inadequate government oversight.\n**(3)**\nMilitary families frequently shoulder the financial burden of environmental hazards, often paying out-of-pocket for temporary relocation, the loss of personal property, medical expenses, and long-term health evaluations and treatments.\n**(4)**\nUnsafe housing conditions undermine military readiness by forcing members of the Armed Forces to divert time and attention from their duties to manage health and housing emergencies, jeopardizing mission performance, morale, and unit cohesion.\n**(5)**\nThe lack of consistent, independent audits, inspections, and performance assessments of privatized military housing has enabled poor contractor accountability, resulting in ongoing maintenance failures and tenant harm.\n**(6)**\nThe use of non-disclosure agreements by providers of privatized military housing to silence tenants reporting unsafe conditions obstructs transparency, suppresses awareness of systemic failures, and impedes efforts to hold contractors accountable.\n**(7)**\nAvailable data from medical reports, tenant surveys, and documentation by the Department of Defense strongly suggest that prolonged exposure to mold in privatized military housing is linked to higher rates of respiratory illness, neurological symptoms, and developmental issues in children, underscoring the urgent need for comprehensive environmental health protections.\n**(8)**\nAs of the date of the enactment of this Act, the TRICARE program (as defined in section 1072 of title 10, United States Code) does not cover mold-related medical expenses, including diagnostic testing for mycotoxin exposure or long-term treatment for illnesses caused or exacerbated by mold, leaving military families without adequate support for housing-related health conditions.\n**(9)**\nApproximately 700,000 members of the Armed Forces and their families reside in privatized military housing operated by 14 companies across 78 developments in the United States.\n**(10)**\nSeveral providers of privatized military housing have been implicated in fraud schemes in recent years, including one company that pled guilty in 2021 to defrauding the Department of Defense by falsifying maintenance records, and another that reached a $500,000 Federal settlement in 2022, without admitting guilt, for similar misconduct.\n#### 3. Development and implementation of minimum health and safety standards for military family housing\n##### (a) Standards\n**(1) Initial guidance**\n**(A) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense shall issue interim guidance for acceptable levels of relative humidity, ventilation, dampness, and water intrusion to be applied at all covered housing.\n**(B) Effect**\nInterim guidance issued under subparagraph (A) shall remain in effect until final standards are published under paragraph (2).\n**(2) Final standards**\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense shall issue final standards for acceptable levels of relative humidity, ventilation, dampness, and water intrusion to be applied at all covered housing, which shall include\u2014\n**(A)**\nacceptable levels of relative humidity indoors;\n**(B)**\nrequired ventilation and moisture control measures;\n**(C)**\nenvironmental inspection and testing methods; and\n**(D)**\nthe standard of care for mold remediation adopted under subsection (g).\n**(3) Reporting and availability of testing**\nThe final standards established under paragraph (2) shall require results of environmental inspection and testing methods under subparagraph (C) of such paragraph to be reported to the Secretary of Defense and made available to tenants of affected housing units not later than 10 days after sample collection.\n##### (b) Certification of compliance\nNot less frequently than annually, each housing office of the Department shall certify to Congress that the housing office is in compliance with health and safety standards for covered housing required under this section.\n##### (c) Establishment of independent inspection protocol for privatized military housing\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense shall ensure that each installation of the Department of Defense conducts, using independent certified third-party inspectors, mold and environmental health inspections for all covered housing that is privatized military housing\u2014\n**(A)**\nupon every tenant turnover of a housing unit;\n**(B)**\nupon receipt of any tenant complaint regarding safety and habitability of a housing unit; and\n**(C)**\nfollowing any remediation effort, structural repair, or response to an identified environmental hazard at a housing unit.\n**(2) Elements of inspections**\nInspections conducted under paragraph (1) shall include, at a minimum\u2014\n**(A)**\nevaluation of heating, ventilation, and air conditioning (HVAC) systems, plumbing, electrical systems, and structural integrity;\n**(B)**\ninspection for signs of water intrusion, dampness, humidity, visible or non-visible mold, microbial growth, and other indoor air quality concerns;\n**(C)**\nreview of current and past work order records and completion timelines; and\n**(D)**\nreview of contractor compliance with privatized military housing contract requirements and housing regulations of the Department of Defense.\n**(3) Recording and maintenance of records**\nAll findings of inspections conducted under paragraph (1) shall be\u2014\n**(A)**\nrecorded in a standardized Federal Government inspection record;\n**(B)**\ncertified by the inspector with a clear pass or fail status;\n**(C)**\nmaintained in an accessible, historical housing record for each housing unit; and\n**(D)**\nmade available to the relevant installation commander and military housing office.\n**(4) Documentation and submission of results**\nThe commander of each installation of the Department shall\u2014\n**(A)**\ndocument results of inspections conducted under paragraph (1); and\n**(B)**\nsubmit the results of such inspections to\u2014\n**(i)**\nthe Secretary;\n**(ii)**\nthe Office of Inspector General of the Department of Defense; and\n**(iii)**\nthe Committees on Armed Services of the Senate and the House of Representatives.\n**(5) Access and transparency**\nInspection reports certified under paragraph (3)(B) and housing history records required under paragraph (3)(C) shall be\u2014\n**(A)**\nprovided in full to current tenants of the inspected unit;\n**(B)**\nmade available upon request to any incoming tenants; and\n**(C)**\nmaintained in a secure portal accessible to staff of the relevant military housing office, the Committees on Armed Services of the Senate and the House of Representatives, and military family advocacy personnel.\n**(6) Remediation or tenant relocation**\nIn the case of a housing unit failing inspection conducted under paragraph (1), the Secretary shall ensure that the unit is remediated or the tenants of such unit are relocated not later than 30 days after such failed inspection, if such tenants wish to be relocated.\n##### (d) Complaint and response mechanism\n**(1) Hotline and website**\nThe Secretary shall modify the Defense Housing Feedback System, or successor system, to ensure that such system contains a tenant complaint hotline and website that is available 24 hours per day, seven days per week for reporting humidity, water damage, or other hazards in covered housing.\n**(2) Website information**\nThe website required under paragraph (1) shall contain information on the complaints made under paragraph (1), disaggregated by installation and with any personally identifying information redacted.\n**(3) Response**\nEach housing office for an installation of the Department shall\u2014\n**(A)**\nrespond to complaints of tenants of covered housing not later than five business days after the complaint;\n**(B)**\ntrack progress of such response until resolution; and\n**(C)**\nprovide to tenants written confirmation of inspection findings and actions taken.\n##### (e) Requirements for privatized military housing\n**(1) Health and safety standards for military housing**\nThe Secretary of each military department shall ensure that all housing project agreements and renewals for privatized military housing under the jurisdiction of the Secretary concerned entered into on or after the date of the enactment of this Act are compliant with the appropriate environmental health and safety standards established by the Department of Defense.\n**(2) Future contract agreements and renewals**\nFor all housing project agreements and renewals for privatized military housing entered into on or after the date of the enactment of this Act, and to the extent practicable for agreements in place as of such date of enactment, not later than 180 days after the date of the enactment of this Act, the Secretary of Defense shall incorporate enforceable provisions related to environmental hazard response, inspection, and tenant relocation protections which shall include\u2014\n**(A)**\nenforceable environmental health and safety clauses; and\n**(B)**\nrequirements that providers of privatized military housing bear full financial responsibility for\u2014\n**(i)**\nrequired third-party inspections;\n**(ii)**\nmaintenance;\n**(iii)**\nmold remediation;\n**(iv)**\nall relocation expenses for military families forced to vacate uninhabitable units;\n**(v)**\nproperty loss; and\n**(vi)**\nrefunding any amounts paid through a basic allowance for housing under section 403 of title 37, United States Code, for military families forced to vacate uninhabitable units.\n##### (f) Certification requirements for mold assessment and remediation\nThe Secretary shall ensure that all maintenance personnel, contracted mold assessors, indoor environmental professionals, and mold remediators responsible for assessing or remediating mold and water damage in covered housing shall possess and maintain current certifications issued by a nationally recognized, third-party, nonprofit certifying body, which may include the following:\n**(1)**\nThe Institute of Inspection Cleaning and Restoration Certification.\n**(2)**\nThe National Organization of Remediators and Microbial Inspectors.\n**(3)**\nThe American Council for Accredited Certification.\n##### (g) Standard of care for mold remediation\nAll mold remediation activities conducted in covered housing shall comply with the American National Standards Institute and Institute of Inspection Cleaning and Restoration Certification S520 Standard for Professional Mold Remediation, Fourth Edition, or any subsequent edition published by the Institute of Inspection Cleaning and Restoration Certification or successor organization.\n##### (h) Issuance of guidance\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall\u2014\n**(1)**\nissue guidance with respect to the implementation of this section; and\n**(2)**\nprovide written notification to all providers of privatized military housing regarding the requirements of this section.\n##### (i) Quarterly reporting requirement\n**(1) Designation of Chief Housing Officer**\nThe Assistant Secretary of Defense for Energy, Installations, and Environment shall serve as Chief Housing Officer and shall receive, review, and compile reports from military housing offices across all installations of the Department of Defense.\n**(2) Military housing office reporting**\nNot less frequently than quarterly, each chief of a military housing office shall submit to the Chief Housing Officer designated under paragraph (1) a report that includes, at a minimum\u2014\n**(A)**\nthe number and type of tenant complaints received;\n**(B)**\nan assessment of work order volume and average completion time;\n**(C)**\nan identification of instances of unresolved or recurring maintenance issues;\n**(D)**\nan identification of environmental hazard notifications and the status of the remediation of such hazards;\n**(E)**\na summary of compliance by contractors with requirements of the Department and any violations of those requirements;\n**(F)**\nany reports of retaliation, discrimination, displacement, or housing-related medical concerns (with personal information redacted if requested); and\n**(G)**\na summary of command-level awareness or action on housing issues.\n**(3) Compilation and congressional submission**\n**(A) In general**\nThe Chief Housing Officer shall\u2014\n**(i)**\ncompile the reports received under paragraph (2);\n**(ii)**\nsubmit to the Committees on Armed Services of the Senate and the House of Representatives such compiled reports not less frequently than quarterly and not less frequently than annually for the quarter or year covered by the report, as the case may be; and\n**(iii)**\nprovide to the Committees on Armed Services of the Senate and the House of Representatives briefings regarding each report submitted under clause (ii).\n**(B) Briefings**\nBriefings required under subparagraph (A)(iii) shall include trend analysis, contractor performance insights, and risk flags based on installation-level conditions.\n**(4) Data transparency and retention**\n**(A) Format**\nThe Secretary shall ensure that all reporting required under this subsection follows a standardized Federal format.\n**(B) Retention of information**\nThe Secretary shall ensure that all raw data, logs, and supporting documentation for reports required under this subsection are retained for a period of not less than five years.\n**(C) Availability of data sets**\nThe Secretary may make available to tenant ombudsmen or Federal housing liaison offices data sets used to prepare reports under this subsection with personally identifiable information redacted.\n**(5) Enforcement**\nIn the case of a landlord (as defined in section 2871 of title 10, United States Code) or other private sector entity that fails to comply with any requirement established to comply with this subsection, the Secretary may\u2014\n**(A)**\nnotify command leadership of the relevant installation of the Department;\n**(B)**\nconduct an audit or performance review; and\n**(C)**\nin the case of systemic failure to comply with any such requirement, suspend eligibility of such landlord or entity for housing-related bonuses.\n##### (j) Public reporting requirements\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the Secretary shall submit to the Committees on Armed Services of the Senate and the House of Representatives and publish on a publicly available website of the Department of Defense, with respect to covered housing\u2014\n**(1)**\nthe number of mold complaints received, disaggregated by installation of the Department;\n**(2)**\nthe results of inspections under this section and compliance rates;\n**(3)**\nremediation timelines and costs; and\n**(4)**\nthe number of relocations made.\n##### (k) Sense of Congress on health risks associated with mold\nIt is the sense of Congress that the Secretary of Defense, in collaboration with the Secretary of Health and Human Services, should evaluate the health impacts of mold exposure in military housing and consider appropriate medical responses and coverage under existing health care systems.\n##### (l) Definitions\nIn this section:\n**(1) Acceptable levels of relative humidity**\nThe term acceptable levels of relative humidity , with respect to an area, means an area with humidity levels that are less than 50 percent.\n**(2) Covered housing**\nThe term covered housing means any military family housing owned, leased, or managed by the Department of Defense, including privatized military housing.\n**(3) Environmental inspection and testing methods**\nThe term environmental inspection and testing methods means detailed visual inspection substantiated by mold testing measures that include air sampling, tape lifts, swabs, and carpet samples, and official laboratory analysis of such samples.\n**(4) Mold**\nThe term mold means any form of multi-cellular fungi found in water-damaged indoor environments and building materials, including, cladosporium, penicillium, alternaria, aspergillus, fusarium, chaetomium, trichoderma, memnoniella, mucor, stachybotrys chartarum, streptomyces, and epicoccumoften.\n**(5) Privatized military housing**\nThe term privatized military housing means military housing under subchapter IV of chapter 169 of title 10, United States Code.",
      "versionDate": "2026-01-21",
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
        "actionDate": "2026-01-15",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "3654",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MOLD Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-02-13T17:57:12Z"
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
      "date": "2026-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7188ih.xml"
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
      "title": "MOLD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MOLD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Military Occupancy Living Defense Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve housing and environmental health and safety protections for members of the Armed Forces and their families residing in military family housing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:03:29Z"
    }
  ]
}
```
