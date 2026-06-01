# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7773?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7773
- Title: Field Integration of Homeland Intelligence Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7773
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-05-16T08:07:39Z
- Update date including text: 2026-05-16T08:07:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-03-04 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-03-04 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7773",
    "number": "7773",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Field Integration of Homeland Intelligence Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:39Z",
    "updateDateIncludingText": "2026-05-16T08:07:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Counterterrorism and Intelligence.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-04T05:00:00Z",
              "name": "Referred to"
            }
          },
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7773ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7773\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Pfluger introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo provide for the decentralization of operation of the DHS Office of Intelligence and Analysis, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Field Integration of Homeland Intelligence Act of 2026 .\n#### 2. Findings; purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe Department of Homeland Security (DHS) currently operates a centralized model for the Office of Intelligence and Analysis (I&A) of the Department, with a significant concentration of analytic functions based in Washington, DC.\n**(2)**\nDHS already maintains a robust ten-region field structure utilized by the Federal Emergency Management Agency (FEMA), the Cybersecurity and Infrastructure Security Agency (CISA), I&A, and other DHS components that should continue to be leveraged to improve intelligence integration.\n**(3)**\nEffective homeland security intelligence requires closer collaboration between Federal partners and State, local, Tribal, and territorial (SLTT) partners, including fusion centers, and joint or interagency task forces.\n**(4)**\nDecentralizing analytic functions will improve operational relevance, responsiveness, and coordination, while generating efficiencies across DHS components and with SLTT partners.\n##### (b) Purpose\nThe purpose of this Act is to restructure DHS I&A operations by ensuring a field-centric intelligence model that places analytic personnel directly in the regions they support, thereby improving interagency collaboration and the effectiveness of homeland security intelligence efforts.\n#### 3. Decentralization of operation of DHS Office of Intelligence and Analysis\n##### (a) In general\n**(1) Decentralization mandate**\nNot later than two years after the date of the enactment of this Act, the Secretary of Homeland Security shall carry out the following:\n**(A)**\nTransition the primary analytic functions of the Office of Intelligence and Analysis of the Department of Homeland Security from a centralized headquarters-based model to a decentralized, field-based model.\n**(B)**\nAssign at least one Intelligence Officer (IO) of the Office to every fusion center, as well as other strategic locations of importance, as determined by the Secretary.\n**(C)**\nAssign at least one Intelligence Analyst (IA) of the Office to every fusion center, as well as other strategic locations of importance, as determined by the Secretary.\n**(D)**\nAssign at least one Intelligence Officer (IO) of the Office to each joint or interagency task force, to serve as the primary Office liaison to ensure real-time analytic support and operational intelligence sharing.\n**(2) Personnel requirements**\n**(A) Prohibition**\nAn individual may not serve concurrently in the IO and IA roles required under paragraph (1).\n**(B) Training**\nThe Secretary shall provide to each IO and IA assigned to a fusion center and or joint or interagency task force training on civil rights, civil liberties, privacy rights, regulations, and information practices pursuant to section 552a of title 5, United States Code (commonly referred to as the Privacy Act of 1974 ), and other relevant laws prior to the official start date of such an IO or IA, as the case may be, at such a fusion center or joint or interagency task force, as the case may be.\n**(C) Consistency of assignments**\nIn assigning an IO and IA to each fusion center pursuant to paragraph (1), the Secretary of Homeland Security shall request and integrate input from the fusion center at issue, to ensure personnel assignments are consistent with the unique needs of such fusion center.\n**(D) Term of assignment**\nThe term of assignment of an IO and IA at a fusion center shall be three years, and may be extended for up to an additional two years at the discretion of the Secretary.\n**(E) Maintenance**\nUpon completion of an IO\u2019s or IA\u2019s assignment at a fusion center, the Secretary shall ensure such IO and IA do not rotate out simultaneously, in order that each fusion center maintains at least one representative of the Office of Intelligence and Analysis of the Department at all times.\n##### (b) Field integration and coordination\n**(1) In general**\nEach assigned IO and IA shall report operationally to the I&A Regional Director of the respective DHS Region, in accordance with policy guidance and functional oversight from the Under Secretary for Intelligence and Analysis of the Department of Homeland Security.\n**(2) Coordination**\nField-based personnel of I&A shall coordinate with regional leads from FEMA, CISA, U.S. Immigration and Customs Enforcement (ICE), U.S. Customs and Border Protection (CBP), and other components of the Department of Homeland Security, to ensure integrated intelligence support for regional priorities.\n##### (c) Resource alignment and personnel\nNot later than 180 days after the date of the enactment of this Act, the Under Secretary for Intelligence and Analysis of the Department of Homeland Security shall submit to the appropriate congressional committees a staffing and resource plan that\u2014\n**(1)**\ndetails the I&A personnel required to staff the Regions;\n**(2)**\nidentifies existing headquarters roles eligible for reassignment to the field;\n**(3)**\nidentifies required staff and resources for headquarters-based analytic, information sharing, management, and oversight functions, including the rationale for the retention at headquarters of any such staff or resources;\n**(4)**\nidentifies how I&A will implement a rotational program to ensure field-based IOs and IAs spend not more than five years in a field location without a headquarters rotation; and\n**(5)**\noutlines additional hiring, training, or realignment necessary to satisfy the decentralization requirement under subsection (a)(1).\n##### (d) Headquarters personnel\nNotwithstanding subsection (a), the Secretary shall assign to headquarters-based functions required staff and resources according to the staffing and resources plan pursuant to subsection (c).\n##### (e) Performance metrics and reporting\n**(1) Initial implementation report**\nNot later than one year after the date of the enactment of this Act, the Secretary of Homeland Security shall submit to the appropriate congressional committees a report that details the following:\n**(A)**\nProgress on decentralization and personnel issues in accordance with paragraphs (1) and (2), respectively, of subsection (a).\n**(B)**\nThe status of resource alignment and personnel issues in accordance with subsection (c).\n**(C)**\nAny barriers or challenges encountered in carrying out such decentralization or reassignments, as the case may be.\n**(2) Annual assessment**\nNot later than one year after the submission of the report required under paragraph (1) and annually thereafter for five years, the Secretary of Homeland Security shall submit to the appropriate congressional committees a report that\u2014\n**(A)**\nassesses\u2014\n**(i)**\nthe operational impact on I&A and SLTT partners of decentralization in accordance with subsection (a)(1);\n**(ii)**\nefficiencies or improvements in intelligence support at the interagency level related to the placement of I&A personnel within the regions supported by such personnel; and\n**(iii)**\nthe extent to which Federal partners and SLTT partners have cohesively integrated to improve operational coordination and information sharing; and\n**(B)**\nincludes a description of the training provided, and copies of the training materials used, pursuant to subsection (a)(2)(B).\n##### (f) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the Committee on Homeland Security of the House of Representatives, the Committee on Homeland Security and Government Affairs of the Senate, the Permanent Select Committee on Intelligence of the House of Representatives, and the Senate Select Committee on Intelligence.\n**(2) Fusion center**\nThe term fusion center has the meaning given such term in section 210A of the Homeland Security Act of 2002 ( 6 U.S.C. 124h ).\n**(3) I&A**\nThe term I&A means the Office of Intelligence and Analysis of the Department of Homeland Security.\n**(4) Region**\nThe term Region means one of the ten standard Federal Emergency Management Agency (FEMA) regions, unless otherwise specified by the Secretary of Homeland Security.",
      "versionDate": "2026-03-03",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-20T19:12:56Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7773ih.xml"
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
      "title": "Field Integration of Homeland Intelligence Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Field Integration of Homeland Intelligence Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the decentralization of operation of the DHS Office of Intelligence and Analysis, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T08:18:22Z"
    }
  ]
}
```
