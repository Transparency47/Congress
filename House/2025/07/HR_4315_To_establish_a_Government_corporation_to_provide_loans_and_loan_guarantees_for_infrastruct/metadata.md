# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4315?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4315
- Title: National Infrastructure Investment Corporation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4315
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2025-09-11T08:06:32Z
- Update date including text: 2025-09-11T08:06:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-11 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-11 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4315",
    "number": "4315",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
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
    "title": "National Infrastructure Investment Corporation Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-11T08:06:32Z",
    "updateDateIncludingText": "2025-09-11T08:06:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-11",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
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
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:07:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-11T19:34:18Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
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
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4315ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4315\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mr. Carbajal (for himself and Mr. Webster of Florida ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish a Government corporation to provide loans and loan guarantees for infrastructure projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Infrastructure Investment Corporation Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAccording to the American Society of Civil Engineers 2025 Infrastructure Report, the current condition of the infrastructure in the United States earns a grade of C and an estimated $3,700,000,000,000 is needed to have infrastructure in good working order.\n**(2)**\nCurrent and foreseeable demands on traditional funding for infrastructure expansion exceed the resources to support much-needed infrastructure programs.\n**(3)**\nAs of April 19, 2019, the top 50 strategic infrastructure projects, including transportation, water and wastewater, ports and waterways, and telecommunications, totaled $289,370,000,000 in unmet needs.\n**(4)**\nInfrastructure needs are not limited to traditional roads and bridges but include a wide sector of basic, physical, and organizational structures and facilities that are needed for the effective and productive operation of society.\n**(5)**\nInvestment in infrastructure not only creates jobs and economic growth and is a key component of maintaining a global competitive edge but is also fundamental to enhancing and preserving quality of life.\n**(6)**\nThe establishment of a Government corporation that provides loans supported by pension funds to finance qualified infrastructure projects would attract needed supplemental capital for infrastructure development.\n#### 3. Establishment\nThere is established a corporation to be known as the National Infrastructure Investment Corporation (in this Act referred to as the Corporation ), which shall be a Government corporation as defined in section 103 of title 5, United States Code, whose purpose shall be to finance infrastructure projects that are beyond the financing capabilities of States and cities, including\u2014\n**(1)**\nprioritizing projects in a fair and efficient manner; and\n**(2)**\nminimizing financial costs to the Federal Government.\n#### 4. Board of Directors and Inspector General\n##### (a) Establishment\nThe management of the Corporation shall be vested in a board of directors (in this Act referred to as the Board ).\n##### (b) Membership\nThe Board shall be composed of 7 members that meet the qualifications under subsection (c), consisting of\u2014\n**(1)**\n3 members appointed by the President, by and with the advice and consent of the Senate;\n**(2)**\n1 member appointed by the majority leader of the Senate;\n**(3)**\n1 member appointed by the minority leader of the Senate;\n**(4)**\n1 member appointed by the Speaker of the House of Representatives; and\n**(5)**\n1 member appointed by the minority leader of the House of Representatives.\n##### (c) Qualifications\nEach member of the Board shall\u2014\n**(1)**\nbe a citizen of the United States;\n**(2)**\nhave significant demonstrated experience or expertise in\u2014\n**(A)**\ninfrastructure, and with respect to infrastructure, experience or expertise in\u2014\n**(i)**\nheavy construction;\n**(ii)**\nlabor; or\n**(iii)**\ngovernment policy;\n**(B)**\nthe financing, development, or operation of infrastructure projects, including the evaluation and selection of eligible projects; or\n**(C)**\nthe management and administration of a financial institution that provides financing for infrastructure projects; and\n**(3)**\nrepresent different geographic regions of the United States to ensure rural areas and small communities are represented.\n##### (d) Initial appointments\nNot later than 30 days after the date of enactment of this Act, the President and congressional leadership shall appoint the members of the Board in accordance with subsections (b) and (c).\n##### (e) Chair\nThe Chair of the Board shall be designated by the President from among the members appointed under subsection (b).\n##### (f) Terms\nEach member of the Board shall hold office for a term of 5 years, except as provided in the following paragraphs:\n**(1) Terms of initial appointees**\nAs designated by the President and congressional leadership at the time of appointment\u2014\n**(A)**\nthe Chair shall be appointed for a term of 5 years;\n**(B)**\nthe 4 members appointed by congressional leadership shall be appointed for a term of 4 years; and\n**(C)**\nthe 2 members appointed by the President shall be appointed for a term of 2 years.\n**(2) Vacancies**\nVacancies shall be filled according to the following:\n**(A)**\nA vacancy shall be filled in the manner in which the original appointment was made.\n**(B)**\nAny Board member elected to fill a vacancy occurring before the expiration of the term for which the direct predecessor of the member was appointed shall be appointed only for the remainder of that term.\n**(C)**\nIn accordance with subparagraph (B), a Board member may serve after the expiration of the term of the direct predecessor of the Board member until a successor has taken office.\n##### (g) Responsibilities of the Board\nThe responsibilities of the Board are as follows:\n**(1)**\nProvide low-cost loans and loan guarantees to eligible applicants under section 5.\n**(2)**\nDevelop strategic goals for the Corporation based on the purpose of the Corporation.\n**(3)**\nMonitor and assess the effectiveness of the Corporation in achieving such strategic goals.\n**(4)**\nReview and approve the annual business plans, annual budgets, and long-term strategies of and for infrastructure projects financed through the Corporation.\n**(5)**\nDevelop, review, and approve annual reports for the Corporation.\n**(6)**\nEmploy at least 1 external auditor to conduct an annual audit of such infrastructure projects.\n**(7)**\nEmploy individuals as necessary to carry out the provisions of this Act.\n**(8)**\nDetermine the operations and internal policies of the Corporation.\n##### (h) Inspector General\nThe Board shall appoint an employee of the Corporation to be known as the Inspector General whose duties shall include the following:\n**(1)**\nConduct audits under section 6(b).\n**(2)**\nCarry out, with respect to the Corporation, duties and responsibilities established under the Inspector General Act of 1978 (5 U.S.C. App.).\n**(3)**\nEstablish, maintain, and oversee such audits as the Inspector General considers appropriate under this Act.\n#### 5. Loans, loan guarantees, and bonding\n##### (a) General authority\nThe Corporation shall provide loans, loan guarantees, and bonds to eligible applicants for infrastructure projects in the United States.\n##### (b) Eligibility requirements\nAn applicant is eligible for a loan, loan guarantee, or bond under this section if the applicant\u2014\n**(1)**\nsubmits a detailed letter of interest to the Corporation that\u2014\n**(A)**\ndescribes the infrastructure project and the location, purpose, and cost of the project;\n**(B)**\noutlines the proposed financial plan with respect to such project, including the requested loan, loan guarantee, or bond amount and the proposed obligor;\n**(C)**\nprovides a status of environmental review; and\n**(D)**\nsummarizes the geographic area affected by such project; and\n**(2)**\nmeets the prerequisites for assistance and conditions for assistance described in subsections (g) and (h) of section 502 of the Railroad Revitalization and Regulatory Reform Act of 1976 ( 45 U.S.C. 822(g) and (h)).\n##### (c) Eligible uses\nLoans, loan guarantees, and bonds provided under this section may be used only for eligible project costs (as defined in section 601(a)(2) of title 23, United States Code) for infrastructure projects, including transportation, energy, environment, and telecommunications.\n##### (d) Consultation\nPrior to approving a loan, loan guarantee, or bond under this section, the Corporation shall require the applicant to consult with any member of the House of Representatives or member of the Senate whose district or State, respectively, is affected by the infrastructure project to ensure that such project is meritorious and to avoid any problems that may arise with respect to such project.\n##### (e) Timing\nA loan or bond provided under subsection (a) shall be structured with respect to the expected timing and duration of the construction and utility of an infrastructure project.\n##### (f) TIFIA\nExcept as inconsistent with this Act, the Corporation shall provide for loans, loan guarantees, and bonds under this section in the same manner and subject to the same requirements as the Secretary of Transportation enters into loans and loan agreements under section 602 of chapter 6 of title 23, United States Code, with respect to the TIFIA program (as defined in section 601 of such title).\n#### 6. Audits and reports\n##### (a) Report to Congress\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Board shall submit to Congress a report on the activities of the Corporation.\n##### (b) Annual audit\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Inspector General of the Corporation shall\u2014\n**(1)**\nconduct an account audit of the Corporation;\n**(2)**\nconduct, supervise, and coordinate investigations of the business activities of the Corporation;\n**(3)**\nensure that the Corporation is acting consistent with this Act; and\n**(4)**\nsubmit the results of such audit to Congress.\n##### (c) GAO audit and report\nNot later than 5 years after the date of enactment of this Act, and every 5 years thereafter, the Comptroller General of the United States shall\u2014\n**(1)**\nconduct an evaluation of the activities of the Corporation from the previous 5 fiscal years; and\n**(2)**\nsubmit to Congress a report containing the results of such evaluation, which shall include\u2014\n**(A)**\nan assessment of the impact and benefits of each infrastructure project financed through the Corporation; and\n**(B)**\na review of the effectiveness of such infrastructure project in accomplishing the goals of this Act.\n##### (d) Application waiting period\nBefore any loan or loan guarantee is awarded under this Act, the Corporation shall submit to Congress a report describing the application for such loan or loan guarantee. The Corporation may not award the loan or loan agreement before the end of the 60-day period following the submission of such report to Congress. The Corporation may award the loan or loan agreement after such period unless Congress enacts a joint resolution disapproving the application with an explanation for such disapproval.\n##### (e) Rejected applications\nAn application that is rejected under subsection (d) shall not be resubmitted to the Corporation unless the basis for the disapproval of the application has been addressed by the resubmitted application.\n#### 7. Funding\n##### (a) Pension fund loans\nFor purposes of paying for the administrative costs of the Corporation and to provide loans and loan guarantees for eligible infrastructure projects, the Board may accept loans during fiscal years 2026 through 2030 from pension funds.\n##### (b) Limitation\nThe Board may not accept more than $5,000,000,000 in loans under subsection (a) during any single fiscal year.\n##### (c) Annual percentage rate\nWith respect to a loan described under subsection (a), the Board may not pay an annual percentage rate of less than 3 percent or more than 4 percent.",
      "versionDate": "2025-07-10",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-10T16:52:56Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4315ih.xml"
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
      "title": "National Infrastructure Investment Corporation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T13:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Infrastructure Investment Corporation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a Government corporation to provide loans and loan guarantees for infrastructure projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T13:48:32Z"
    }
  ]
}
```
