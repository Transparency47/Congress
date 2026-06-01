# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/323?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/323
- Title: PLAN for Broadband Act
- Congress: 119
- Bill type: S
- Bill number: 323
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2026-05-23T06:53:30Z
- Update date including text: 2026-05-23T06:53:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.
- 2026-05-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. Without written report.
- 2026-05-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. Without written report.
- 2026-05-21 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 421.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.
- 2026-05-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. Without written report.
- 2026-05-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. Without written report.
- 2026-05-21 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 421.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/323",
    "number": "323",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "W000437",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Wicker, Roger F. [R-MS]",
        "lastName": "Wicker",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "PLAN for Broadband Act",
    "type": "S",
    "updateDate": "2026-05-23T06:53:30Z",
    "updateDateIncludingText": "2026-05-23T06:53:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 421.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
            "date": "2026-05-21T18:59:30Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-12T14:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-12T14:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-29T23:28:28Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "NM"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s323is.xml",
      "text": "ii\n119th CONGRESS\n1st Session\nS. 323\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Wicker (for himself, Mr. Luj\u00e1n , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo direct the Assistant Secretary of Commerce for Communications and Information to develop a National Strategy to Synchronize Federal Broadband Programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Proper Leadership to Align Networks for Broadband Act or the PLAN for Broadband Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate; and\n**(B)**\nthe Committee on Energy and Commerce of the House of Representatives.\n**(2) Assistant Secretary**\nThe term Assistant Secretary means the Assistant Secretary of Commerce for Communications and Information.\n**(3) Broadband internet access service**\nThe term broadband internet access service has the meaning given the term in section 8.1(b) of title 47, Code of Federal Regulations, or any successor regulation.\n**(4) Covered agencies**\nThe term covered agencies means\u2014\n**(A)**\nthe Federal Communications Commission;\n**(B)**\nthe Department of Agriculture;\n**(C)**\nthe National Telecommunications and Information Administration;\n**(D)**\nthe Department of Health and Human Services;\n**(E)**\nthe Appalachian Regional Commission;\n**(F)**\nthe Delta Regional Authority;\n**(G)**\nthe Denali Commission;\n**(H)**\nthe Economic Development Administration;\n**(I)**\nthe Department of Education;\n**(J)**\nthe Department of the Treasury;\n**(K)**\nthe Department of Transportation;\n**(L)**\nthe Institute of Museum and Library Services;\n**(M)**\nthe Northern Border Regional Commission;\n**(N)**\nthe Department of Housing and Urban Development; and\n**(O)**\nthe Department of the Interior.\n**(5) Deployment Locations Map**\nThe term Deployment Locations Map has the meaning given the term in section 60105(a) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704(a) ).\n**(6) Federal broadband program**\nThe term Federal broadband program means any program administered by a covered agency that is directly or indirectly intended to increase the deployment of, access to, the affordability of, or the adoption of broadband internet access service.\n**(7) Federal land management agency**\nThe term Federal land management agency means\u2014\n**(A)**\nthe National Park Service;\n**(B)**\nthe Bureau of Land Management;\n**(C)**\nthe Bureau of Reclamation;\n**(D)**\nthe United States Fish and Wildlife Service;\n**(E)**\nthe Bureau of Indian Affairs; and\n**(F)**\nthe Forest Service.\n**(8) Implementation plan**\nThe term Implementation Plan means the implementation plan developed under section 4(a).\n**(9) Strategy**\nThe term Strategy means the National Strategy to Synchronize Federal Broadband Programs developed under section 3(a).\n#### 3. National strategy to synchronize Federal broadband programs\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Assistant Secretary, in consultation with the covered agencies, shall develop and submit to the appropriate committees of Congress a National Strategy to Synchronize Federal Broadband Programs to\u2014\n**(1)**\nsupport better management of Federal broadband programs to deliver on the goal of providing access to high-speed, affordable broadband internet access service to all individuals in the United States, while ensuring that funding for Federal broadband programs is used in the most efficient and fiscally responsible manner;\n**(2)**\nsynchronize interagency coordination among covered agencies for Federal broadband programs;\n**(3)**\nsynchronize interagency coordination regarding the process for approving the grant of any permit, easement, right of way, or lease to, in, over, or on a building or any other property owned by the Federal Government for the right to install, construct, modify, or maintain infrastructure with respect to broadband internet access service; and\n**(4)**\nreduce unnecessary barriers, eliminate unnecessary costs, and ease administrative burdens to participate in Federal broadband programs.\n##### (b) Requirements\nThe Strategy shall\u2014\n**(1)**\nlist all\u2014\n**(A)**\nFederal broadband programs; and\n**(B)**\nprograms that exist at the State and local levels that are directly or indirectly intended to increase the deployment of, access to, the affordability of, or the adoption of broadband internet access service;\n**(2)**\ndescribe current, as of the date on which the Strategy is submitted, Federal efforts to coordinate Federal broadband programs;\n**(3)**\nidentify gaps and limitations, including laws, regulations, and covered agency policies and practices, that hinder, or may hinder, coordination across Federal broadband programs;\n**(4)**\nestablish clear roles and responsibilities for the covered agencies, as well as clear goals, objectives, and performance measures, for\u2014\n**(A)**\nthe management of all Federal broadband programs; and\n**(B)**\ninteragency coordination efforts with respect to Federal broadband programs;\n**(5)**\naddress the cost of the Strategy, the sources and types of resources and investments needed to carry out the Strategy, and where those resources and investments should be targeted based on balancing risk reductions with costs;\n**(6)**\naddress factors that increase the costs and administrative burdens of participation in Federal broadband programs, including with respect to access to infrastructure necessary for deployment of broadband internet access service;\n**(7)**\nreport information on the effectiveness of each Federal broadband program in terms of how many locations received broadband internet access service or other assistance under each Federal broadband program;\n**(8)**\naddress the extent to which covered agency policies and practices do or do not establish a technologically neutral program;\n**(9)**\nrecommend incentives, legislative solutions, and administrative actions to help State, local, and Tribal governments more efficiently\u2014\n**(A)**\ndistribute, and effectively administer, funding received from Federal broadband programs and avoid duplication of\u2014\n**(i)**\nexisting infrastructure with respect to broadband internet access service; and\n**(ii)**\nfunded projects with respect to broadband internet access service or such projects otherwise subject to enforceable deployment obligations;\n**(B)**\nresolve conflicts with respect to the funding described in subparagraph (A);\n**(C)**\nuse the Deployment Locations Map as a key resource in carrying out subparagraphs (A) and (B); and\n**(D)**\npromote access to infrastructure or rights of way necessary for deployment of broadband internet access service, whether privately or government owned or cooperatively organized for broadband communications;\n**(10)**\nrecommend incentives, legislative solutions, and administrative actions to\u2014\n**(A)**\nimprove the coordination and management of Federal broadband programs; and\n**(B)**\neliminate duplication with respect to Federal broadband programs and non-Federal programs with respect to broadband internet access service;\n**(11)**\ndescribe current, as of the date on which the Strategy is submitted, efforts by covered agencies, Federal land management agencies, and State, local, and Tribal governments to streamline the process for granting a permit or access to an easement, right of way, or lease to, in, over, or on a building or any other property owned or controlled by a government for the right to install, construct, modify, or maintain infrastructure with respect to broadband internet access service;\n**(12)**\nidentify gaps and limitations with respect to allowing regional, interstate, or cross-border economic development organizations to participate in Federal broadband programs;\n**(13)**\naddress specific issues relating to closing the gap on Tribal lands with respect to broadband internet access service; and\n**(14)**\nidentify measures to prevent fraud and misuse of amounts made available to carry out Federal broadband programs, ensure accountability for the use of such funding, and implement effective reporting requirements to measure the success of Federal broadband programs.\n#### 4. Implementation plan\n##### (a) In general\nNot later than 120 days after the date on which the Assistant Secretary submits the Strategy to the appropriate committees of Congress under section 3(a), the Assistant Secretary shall develop and submit to the appropriate committees of Congress an implementation plan for the Strategy.\n##### (b) Implementation plan\nThe Implementation Plan shall, at a minimum\u2014\n**(1)**\nprovide a plan for implementing the roles, responsibilities, goals, objectives, and performance measures for the management of Federal broadband programs and interagency coordination efforts identified in the Strategy;\n**(2)**\nif the Strategy identifies policy and practices that result in programmatic differences among covered agencies with respect to Federal broadband programs, provide a plan to streamline and create consistent policies and practices across all covered agencies for the purposes of Federal broadband programs;\n**(3)**\nfor Federal broadband programs that are not technologically neutral, determine a ceiling on the amount of a subsidy or funding award to provide broadband internet access service to a single location, to be consistently applied and adopted by all covered agencies for the funding of infrastructure with respect to broadband internet access service;\n**(4)**\nprovide a plan for holding the covered agencies accountable for the roles, responsibilities, goals, objectives, and performance measures identified in the Strategy;\n**(5)**\ndescribe the roles and responsibilities of the covered agencies, and the interagency mechanisms, to coordinate the implementation of the Strategy;\n**(6)**\nprovide a plan for coordination among Federal broadband programs and for permitting processes for infrastructure with respect to broadband internet access service;\n**(7)**\nprovide a plan for regular evaluation and public reporting of Federal broadband programs against clear objectives and performance measures, permitting processes for infrastructure with respect to broadband internet access service, and progress in implementing the Strategy;\n**(8)**\nwith respect to the awarding of Federal funds or subsidies to support the deployment of broadband internet access service, provide a plan for the adoption of\u2014\n**(A)**\ncommon data sets regarding those awards, including a requirement that covered agencies use the maps created under title VIII of the Communications Act of 1934 ( 47 U.S.C. 641 et seq. ) and the Deployment Locations Map;\n**(B)**\napplications regarding those awards, as described in section 903(e) of the ACCESS BROADBAND Act ( 47 U.S.C. 1307(e) ); and\n**(C)**\nrules for prohibiting awards by covered agencies in areas identified as served by the maps created under title VIII of the Communications Act of 1934 ( 47 U.S.C. 641 et seq. ) or in areas already subject to an award or enforceable deployment obligations by a covered agency under a Federal broadband program or a State, local, or Tribal program with respect to broadband internet access service;\n**(9)**\nprovide a plan to monitor, publicly report, and reduce waste, fraud, and abuse in Federal broadband programs, including wasteful spending resulting from fragmented, overlapping, and duplicative programs;\n**(10)**\nrequire consistent obligation and expenditure reporting by covered agencies for Federal broadband programs, which shall be consistent with section 903(c)(2) of the ACCESS BROADBAND Act ( 47 U.S.C. 1307(c)(2) ) and the Deployment Locations Map;\n**(11)**\nprovide a plan to increase awareness of, and participation in, Federal broadband programs relating to the affordability and adoption of broadband internet access service; and\n**(12)**\ndescribe the administrative and legislative action that is necessary to carry out the Strategy.\n##### (c) Public comment\nIn developing the Implementation Plan, the Assistant Secretary shall publish a draft version of the Implementation Plan in the Federal Register for a period of notice and comment (and reply comment) that is not less than 60 days.\n#### 5. Briefings and implementation\n##### (a) Briefing\nNot later than 21 days after the date on which the Assistant Secretary submits the Implementation Plan to the appropriate committees of Congress under section 4(a), the Assistant Secretary, and appropriate representatives from the covered agencies involved in the formulation of the Strategy, shall provide a briefing on the implementation of the Strategy to the appropriate committees of Congress.\n##### (b) Implementation\n**(1) In general**\nThe Assistant Secretary shall\u2014\n**(A)**\nimplement the Strategy in accordance with the terms of the Implementation Plan; and\n**(B)**\nnot later than 90 days after the date on which the Assistant Secretary begins to implement the Strategy, and not less frequently than once every 90 days thereafter until the date on which the Implementation Plan is fully implemented, brief the appropriate committees of Congress on the progress in implementing the Implementation Plan.\n**(2) Rule of construction**\nNothing in this subsection may be construed to affect the authority or jurisdiction of the Federal Communications Commission or confer upon the Assistant Secretary or any executive agency the power to direct the actions of the Federal Communications Commission, either directly or indirectly.\n#### 6. Government Accountability Office study and report\nNot later than 1 year after the date on which the Assistant Secretary submits the Implementation Plan to the appropriate committees of Congress under section 4(a), the Comptroller General of the United States shall commence a study\u2014\n**(1)**\nthat shall\u2014\n**(A)**\nexamine the efficacy of the Strategy and the Implementation Plan in coordinating funding across the Federal Government with respect to broadband internet access service;\n**(B)**\nmake recommendations regarding how to improve the Strategy and the Implementation Plan;\n**(C)**\nexamine any existing or new performance goals and measures for Federal broadband programs;\n**(D)**\nexamine any awards made by covered agencies under Federal broadband programs, or under State, local, and Tribal programs with respect to broadband internet access service\u2014\n**(i)**\nin areas identified as served with respect to broadband internet access service; or\n**(ii)**\nthat are duplicative of other awards under such a program; and\n**(E)**\nidentify programmatic changes that would prevent occurrences described in subparagraph (D) in the future; and\n**(2)**\nthe results of which the Comptroller General shall submit to the appropriate committees of Congress.\n#### 7. Broadband funding map reporting\n##### (a) In general\nNot later than 60 days after the date of enactment of this Act, the head of each covered agency shall submit to the Assistant Secretary and the appropriate committees of Congress a report containing a comprehensive update on the measures that each respective covered agency has taken since May 15, 2023, to coordinate with the National Telecommunications and Information Administration, pursuant to subsection (c)(2)(A) of the ACCESS BROADBAND Act ( 47 U.S.C. 1307(c)(2)(A) ), and the Federal Communications Commission to populate the Deployment Locations Map.\n##### (b) Contents\nEach report required under subsection (a) shall include\u2014\n**(1)**\na description of the extent to which the covered agency submitting the report is submitting the data necessary to populate the Deployment Locations Map in a complete and timely manner; and\n**(2)**\nidentification of any outstanding challenges associated with the requirement for the submission of data described in paragraph (1).\n#### 8. Tracking and improving processing times for communications use applications\nSection 6409(b)(3) of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1455(b)(3) ) is amended by adding at the end the following:\n(E) Tracking and improving processing times (i) Data controls An executive agency shall develop controls to ensure that data is sufficiently accurate and complete to track the processing time for each application described in subparagraph (A). (ii) Requirement to analyze, address, and report on delay factors With respect to the factors that contribute to delays in processing applications described in subparagraph (A), an executive agency shall\u2014 (I) analyze the factors as the delays are occurring; (II) take actions to address the factors; and (III) provide an annual report on the factors to\u2014 (aa) the Committee on Commerce, Science, and Transportation of the Senate; (bb) the Committee on Energy and Natural Resources of the Senate; (cc) the Committee on Energy and Commerce of the House of Representatives; (dd) the Committee on Natural Resources of the House of Representatives; and (ee) each committee of Congress with jurisdiction over the executive agency. (iii) Method for alerting staff to at-risk applications An executive agency shall establish a method to alert employees of the executive agency to any application described in subparagraph (A) with respect to which the executive agency is at risk of failing to meet the 270-day deadline under that subparagraph. .\n#### 9. Minimum broadband project cost\nSection 41001(6)(A) of the FAST Act ( 42 U.S.C. 4370m(6)(A) ) is amended\u2014\n**(1)**\nin clause (iii)(III), by striking or at the end;\n**(2)**\nby redesignating clause (iv) as clause (v); and\n**(3)**\nby inserting after clause (iii) the following:\n(iv) (I) is subject to NEPA; (II) involves the construction of infrastructure for broadband; and (III) is likely to require a total investment of more than $5,000,000; or .\n#### 10. Rule of construction\nNothing in this Act, or any amendment made by this Act, may be construed to confer authority on the Federal Government, or any State, local, or Tribal government, to regulate broadband internet access service.",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s323rs.xml",
      "text": "II\nCalendar No. 421\n119th CONGRESS\n2d Session\nS. 323\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Wicker (for himself, Mr. Luj\u00e1n , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nMay 21, 2026 Reported by Mr. Cruz , with amendments Omit the parts struck through and insert the parts printed in italic\nA BILL\nTo direct the Assistant Secretary of Commerce for Communications and Information to develop a National Strategy to Synchronize Federal Broadband Programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Proper Leadership to Align Networks for Broadband Act or the PLAN for Broadband Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate; and\n**(B)**\nthe Committee on Energy and Commerce of the House of Representatives.\n**(2) Assistant Secretary**\nThe term Assistant Secretary means the Assistant Secretary of Commerce for Communications and Information.\n**(3) Broadband internet access service**\nThe term broadband internet access service has the meaning given the term in section 8.1(b) of title 47, Code of Federal Regulations, or any successor regulation.\n**(4) Covered agencies**\nThe term covered agencies means\u2014\n**(A)**\nthe Federal Communications Commission;\n**(B)**\nthe Department of Agriculture;\n**(C)**\nthe National Telecommunications and Information Administration;\n**(D)**\nthe Department of Health and Human Services;\n**(E)**\nthe Appalachian Regional Commission;\n**(F)**\nthe Delta Regional Authority;\n**(G)**\nthe Denali Commission;\n**(H)**\nthe Economic Development Administration;\n**(I)**\nthe Department of Education;\n**(J)**\nthe Department of the Treasury;\n**(K)**\nthe Department of Transportation;\n**(L)**\nthe Institute of Museum and Library Services;\n**(M)**\nthe Northern Border Regional Commission;\n**(N)**\nthe Department of Housing and Urban Development; and\n**(O)**\nthe Department of the Interior.\n**(5) Deployment Locations Map**\nThe term Deployment Locations Map has the meaning given the term in section 60105(a) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1704(a) ).\n**(6) Federal broadband program**\nThe term Federal broadband program means any program administered by a covered agency that is directly or indirectly intended to increase the deployment of, access to, the affordability of, or the adoption of broadband internet access service.\n**(7) Federal land management agency**\nThe term Federal land management agency means\u2014\n**(A)**\nthe National Park Service;\n**(B)**\nthe Bureau of Land Management;\n**(C)**\nthe Bureau of Reclamation;\n**(D)**\nthe United States Fish and Wildlife Service;\n**(E)**\nthe Bureau of Indian Affairs; and\n**(F)**\nthe Forest Service.\n**(8) Implementation plan**\nThe term Implementation Plan means the implementation plan developed under section 4(a).\n**(9) Strategy**\nThe term Strategy means the National Strategy to Synchronize Federal Broadband Programs developed under section 3(a).\n#### 3. National strategy to synchronize Federal broadband programs\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Assistant Secretary, in consultation with the covered agencies, shall develop and submit to the appropriate committees of Congress a National Strategy to Synchronize Federal Broadband Programs to\u2014\n**(1)**\nsupport better management of Federal broadband programs to deliver on the goal of providing access to high-speed, affordable broadband internet access service to all individuals in the United States, while ensuring that funding for Federal broadband programs is used in the most efficient and fiscally responsible manner;\n**(2)**\nsynchronize interagency coordination among covered agencies for Federal broadband programs;\n**(3)**\nsynchronize interagency coordination regarding the process for approving the grant of any permit, easement, right of way, or lease to, in, over, or on a building or any other property owned by the Federal Government for the right to install, construct, modify, or maintain infrastructure with respect to broadband internet access service; and\n**(4)**\nreduce unnecessary barriers, eliminate unnecessary costs, and ease administrative burdens to participate in Federal broadband programs.\n##### (b) Requirements\nThe Strategy shall\u2014\n**(1)**\nlist all\u2014\n**(A)**\nFederal broadband programs; and\n**(B)**\nprograms that exist at the State and local levels that are directly or indirectly intended to increase the deployment of, access to, the affordability of, or the adoption of broadband internet access service;\n**(2)**\ndescribe current, as of the date on which the Strategy is submitted, Federal efforts to coordinate Federal broadband programs;\n**(3)**\nidentify gaps and limitations, including laws, regulations, and covered agency policies and practices, that hinder, or may hinder, coordination across Federal broadband programs;\n**(4)**\nestablish clear roles and responsibilities for the covered agencies, as well as clear goals, objectives, and performance measures, for\u2014\n**(A)**\nthe management of all Federal broadband programs; and\n**(B)**\ninteragency coordination efforts with respect to Federal broadband programs;\n**(5)**\naddress the cost of the Strategy, the sources and types of resources and investments needed to carry out the Strategy, and where those resources and investments should be targeted based on balancing risk reductions with costs;\n**(6)**\naddress factors that increase the costs and administrative burdens of participation in Federal broadband programs, including with respect to access to infrastructure necessary for deployment of broadband internet access service;\n**(7)**\nreport information on the effectiveness of each Federal broadband program in terms of how many locations received broadband internet access service or other assistance under each Federal broadband program;\n**(8)**\naddress the extent to which covered agency policies and practices do or do not establish a technologically neutral program;\n**(9)**\nrecommend incentives, legislative solutions, and administrative actions to help State, local, and Tribal governments more efficiently\u2014\n**(A)**\ndistribute, and effectively administer, funding received from Federal broadband programs and avoid duplication of\u2014\n**(i)**\nexisting infrastructure with respect to broadband internet access service; and\n**(ii)**\nfunded projects with respect to broadband internet access service or such projects otherwise subject to enforceable deployment obligations;\n**(B)**\nresolve conflicts with respect to the funding described in subparagraph (A);\n**(C)**\nuse the Deployment Locations Map as a key resource in carrying out subparagraphs (A) and (B); and\n**(D)**\npromote the safe access to infrastructure or rights of way necessary for deployment of broadband internet access service, whether privately or government owned or cooperatively organized for broadband communications;\n**(10)**\nrecommend incentives, legislative solutions, and administrative actions to\u2014\n**(A)**\nimprove the coordination and management of Federal broadband programs; and\n**(B)**\neliminate duplication with respect to Federal broadband programs and non-Federal programs with respect to broadband internet access service;\n**(11)**\ndescribe current, as of the date on which the Strategy is submitted, efforts by covered agencies, Federal land management agencies, and State, local, and Tribal governments to streamline the process for granting a permit or access to an easement, right of way, or lease to, in, over, or on a building or any other property owned or controlled by a government for the right to install, construct, modify, or maintain infrastructure with respect to broadband internet access service;\n**(12)**\nidentify gaps and limitations with respect to allowing regional, interstate, or cross-border economic development organizations to participate in Federal broadband programs;\n**(13)**\nwith respect to the funding of infrastructure, propose a maximum amount for a subsidy or funding award to provide broadband internet access service to a single location, while allowing for consideration of high cost areas, including high cost Tribal areas;\n**(13) (14)**\naddress specific issues relating to closing the gap on Tribal lands with respect to broadband internet access service; and\n**(14) (15)**\nidentify measures to prevent fraud and misuse of amounts made available to carry out Federal broadband programs, ensure accountability for the use of such funding, and implement effective reporting requirements to measure the success of Federal broadband programs.\n#### 4. Implementation plan\n##### (a) In general\nNot later than 120 days after the date on which the Assistant Secretary submits the Strategy to the appropriate committees of Congress under section 3(a), the Assistant Secretary shall develop and submit to the appropriate committees of Congress an implementation plan for the Strategy.\n##### (b) Implementation plan\nThe Implementation Plan shall, at a minimum\u2014\n**(1)**\nprovide a plan for implementing the roles, responsibilities, goals, objectives, and performance measures for the management of Federal broadband programs and interagency coordination efforts identified in the Strategy;\n**(2)**\nif the Strategy identifies policy and practices that result in programmatic differences among covered agencies with respect to Federal broadband programs, provide a plan to streamline and create consistent policies and practices across all covered agencies for the purposes of Federal broadband programs;\n**(3)**\nfor Federal broadband programs that are not technologically neutral, determine a ceiling on the amount of a subsidy or funding award to provide broadband internet access service to a single location, to be consistently applied and adopted by all covered agencies for the funding of infrastructure with respect to broadband internet access service;\n**(4) (3)**\nprovide a plan for holding the covered agencies accountable for the roles, responsibilities, goals, objectives, and performance measures identified in the Strategy;\n**(5) (4)**\ndescribe the roles and responsibilities of the covered agencies, and the interagency mechanisms, to coordinate the implementation of the Strategy;\n**(6) (5)**\nprovide a plan for coordination among Federal broadband programs and for permitting processes for infrastructure with respect to broadband internet access service;\n**(7) (6)**\nprovide a plan for regular evaluation and public reporting of Federal broadband programs against clear objectives and performance measures, permitting processes for infrastructure with respect to broadband internet access service, and progress in implementing the Strategy;\n**(8) (7)**\nwith respect to the awarding of Federal funds or subsidies to support the deployment of broadband internet access service, provide a plan for the adoption of\u2014\n**(A)**\ncommon data sets regarding those awards, including a requirement that covered agencies use the maps created under title VIII of the Communications Act of 1934 ( 47 U.S.C. 641 et seq. ) and the Deployment Locations Map;\n**(B)**\napplications regarding those awards, as described in section 903(e) of the ACCESS BROADBAND Act ( 47 U.S.C. 1307(e) ); and\n**(C)**\nrules for prohibiting awards by covered agencies in areas identified as served by the maps created under title VIII of the Communications Act of 1934 ( 47 U.S.C. 641 et seq. ) or in areas already subject to an award or enforceable deployment obligations by a covered agency under a Federal broadband program or a State, local, or Tribal program with respect to broadband internet access service;\n**(9) (8)**\nprovide a plan to monitor, publicly report, and reduce waste, fraud, and abuse in Federal broadband programs, including wasteful spending resulting from fragmented, overlapping, and duplicative programs;\n**(10) (9)**\nrequire consistent obligation and expenditure reporting by covered agencies for Federal broadband programs, which shall be consistent with section 903(c)(2) of the ACCESS BROADBAND Act ( 47 U.S.C. 1307(c)(2) ) and the Deployment Locations Map;\n**(11) (10)**\nprovide a plan to increase awareness of, and participation in, Federal broadband programs relating to the affordability and adoption of broadband internet access service; and\n**(12) (11)**\ndescribe the administrative and legislative action that is necessary to carry out the Strategy.\n##### (c) Public comment\nIn developing the Implementation Plan, the Assistant Secretary shall publish a draft version of the Implementation Plan in the Federal Register for a period of notice and comment (and reply comment) that is not less than 60 days.\n#### 5. Briefings and implementation\n##### (a) Briefing\nNot later than 21 days after the date on which the Assistant Secretary submits the Implementation Plan to the appropriate committees of Congress under section 4(a), the Assistant Secretary, and appropriate representatives from the covered agencies involved in the formulation of the Strategy, shall provide a briefing on the implementation of the Strategy to the appropriate committees of Congress.\n##### (b) Implementation\n**(1) In general**\nThe Assistant Secretary shall\u2014\n**(A)**\nimplement the Strategy in accordance with the terms of the Implementation Plan; and\n**(B)**\nnot later than 90 days after the date on which the Assistant Secretary begins to implement the Strategy, and not less frequently than once every 90 days thereafter until the date on which the Implementation Plan is fully implemented, brief the appropriate committees of Congress on the progress in implementing the Implementation Plan.\n**(2) Rule of construction**\nNothing in this subsection may be construed to affect the authority or jurisdiction of the Federal Communications Commission or confer upon the Assistant Secretary or any executive agency the power to direct the actions of the Federal Communications Commission, either directly or indirectly.\n#### 6. Government Accountability Office study and report\nNot later than 1 year after the date on which the Assistant Secretary submits the Implementation Plan to the appropriate committees of Congress under section 4(a), the Comptroller General of the United States shall commence a study\u2014\n**(1)**\nthat shall\u2014\n**(A)**\nexamine the efficacy of the Strategy and the Implementation Plan in coordinating funding across the Federal Government with respect to broadband internet access service;\n**(B)**\nmake recommendations regarding how to improve the Strategy and the Implementation Plan;\n**(C)**\nexamine any existing or new performance goals and measures for Federal broadband programs;\n**(D)**\nexamine any awards made by covered agencies under Federal broadband programs, or under State, local, and Tribal programs with respect to broadband internet access service\u2014\n**(i)**\nin areas identified as served with respect to broadband internet access service; or\n**(ii)**\nthat are duplicative of other awards under such a program; and\n**(E)**\nidentify programmatic changes that would prevent occurrences described in subparagraph (D) in the future; and\n**(2)**\nthe results of which the Comptroller General shall submit to the appropriate committees of Congress.\n#### 7. Broadband funding map reporting\n##### (a) In general\nNot later than 60 days after the date of enactment of this Act, the head of each covered agency shall submit to the Assistant Secretary and the appropriate committees of Congress a report containing a comprehensive update on the measures that each respective covered agency has taken since May 15, 2023, to coordinate with the National Telecommunications and Information Administration, pursuant to subsection (c)(2)(A) of the ACCESS BROADBAND Act ( 47 U.S.C. 1307(c)(2)(A) ), and the Federal Communications Commission to populate the Deployment Locations Map.\n##### (b) Contents\nEach report required under subsection (a) shall include\u2014\n**(1)**\na description of the extent to which the covered agency submitting the report is submitting the data necessary to populate the Deployment Locations Map in a complete and timely manner; and\n**(2)**\nidentification of any outstanding challenges associated with the requirement for the submission of data described in paragraph (1).\n#### 8. Tracking and improving processing times for communications use applications\nSection 6409(b)(3) of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1455(b)(3) ) is amended by adding at the end the following:\n(E) Tracking and improving processing times (i) Data controls An executive agency shall develop controls to ensure that data is sufficiently accurate and complete to track the processing time for each application described in subparagraph (A). (ii) Requirement to analyze, address, and report on delay factors With respect to the factors that contribute to delays in processing applications described in subparagraph (A), an executive agency shall\u2014 (I) analyze the factors as the delays are occurring; (II) take actions to address the factors; and (III) provide an annual report on the factors to\u2014 (aa) the Committee on Commerce, Science, and Transportation of the Senate; (bb) the Committee on Energy and Natural Resources of the Senate; (cc) the Committee on Energy and Commerce of the House of Representatives; (dd) the Committee on Natural Resources of the House of Representatives; and (ee) each committee of Congress with jurisdiction over the executive agency. (iii) Method for alerting staff to at-risk applications An executive agency shall establish a method to alert employees of the executive agency to any application described in subparagraph (A) with respect to which the executive agency is at risk of failing to meet the 270-day deadline under that subparagraph. .\n#### 9. Minimum broadband project cost\nSection 41001(6)(A) of the FAST Act ( 42 U.S.C. 4370m(6)(A) ) is amended\u2014\n**(1)**\nin clause (iii)(III), by striking or at the end;\n**(2)**\nby redesignating clause (iv) as clause (v); and\n**(3)**\nby inserting after clause (iii) the following:\n(iv) (I) is subject to NEPA; (II) involves the construction of infrastructure for broadband; and (III) is likely to require a total investment of more than $5,000,000; or .\n#### 10. Rule of construction\nNothing in this Act, or any amendment made by this Act, may be construed to confer authority on the Federal Government, or any State, local, or Tribal government, to regulate broadband internet access service.",
      "versionDate": "2026-05-21",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-03-05",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S1581)"
      },
      "number": "866",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Accelerating Broadband Permits Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Broadcasting, cable, digital technologies",
            "updateDate": "2025-03-20T13:49:31Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-20T13:48:41Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-03-20T13:56:46Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-20T13:48:41Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-03-20T13:48:41Z"
          },
          {
            "name": "Technology assessment",
            "updateDate": "2025-03-20T13:56:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-07T15:48:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119s323",
          "measure-number": "323",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-07-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s323v00",
            "update-date": "2025-07-16"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Proper Leadership to Align Networks for Broadband Act or the PLAN for Broadband Act</strong></p><p>This bill requires the National Telecommunications and Information Administration (NTIA) to develop and implement a national strategy to improve the coordination and management of federal broadband programs and agency consideration of applications to build or maintain broadband infrastructure on federal property.\u00a0</p><p>The NTIA must also develop and publish for public comment a plan for the implementation of the national strategy. Among other requirements, the implementation plan must establish, for federal broadband programs that are not technologically neutral (i.e., programs\u00a0that involve a preference for certain broadband technologies), a ceiling on the amount of funding that may be awarded to support the provision of broadband service to a single location.\u00a0</p><p>The bill also requires executive branch agencies to identify and address factors that contribute to delays in their review of applications for easements, rights-of-way, or leases related to communications infrastructure projects on federal property. (Under current law, agencies are generally required to act on such applications within 270 days.) Agencies must also establish methods to alert employees when the agency is at risk of failing to meet the 270-day deadline with respect to a particular application.\u00a0</p><p>Finally, the bill lowers the cost threshold for certain broadband infrastructure projects to qualify as <em>covered projects</em> under the Fixing America's Surface Transportation (FAST) Act from $200 million to $5 million. Such projects qualify for expedited federal environmental review.</p>"
        },
        "title": "PLAN for Broadband Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s323.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Proper Leadership to Align Networks for Broadband Act or the PLAN for Broadband Act</strong></p><p>This bill requires the National Telecommunications and Information Administration (NTIA) to develop and implement a national strategy to improve the coordination and management of federal broadband programs and agency consideration of applications to build or maintain broadband infrastructure on federal property.\u00a0</p><p>The NTIA must also develop and publish for public comment a plan for the implementation of the national strategy. Among other requirements, the implementation plan must establish, for federal broadband programs that are not technologically neutral (i.e., programs\u00a0that involve a preference for certain broadband technologies), a ceiling on the amount of funding that may be awarded to support the provision of broadband service to a single location.\u00a0</p><p>The bill also requires executive branch agencies to identify and address factors that contribute to delays in their review of applications for easements, rights-of-way, or leases related to communications infrastructure projects on federal property. (Under current law, agencies are generally required to act on such applications within 270 days.) Agencies must also establish methods to alert employees when the agency is at risk of failing to meet the 270-day deadline with respect to a particular application.\u00a0</p><p>Finally, the bill lowers the cost threshold for certain broadband infrastructure projects to qualify as <em>covered projects</em> under the Fixing America's Surface Transportation (FAST) Act from $200 million to $5 million. Such projects qualify for expedited federal environmental review.</p>",
      "updateDate": "2025-07-16",
      "versionCode": "id119s323"
    },
    "title": "PLAN for Broadband Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Proper Leadership to Align Networks for Broadband Act or the PLAN for Broadband Act</strong></p><p>This bill requires the National Telecommunications and Information Administration (NTIA) to develop and implement a national strategy to improve the coordination and management of federal broadband programs and agency consideration of applications to build or maintain broadband infrastructure on federal property.\u00a0</p><p>The NTIA must also develop and publish for public comment a plan for the implementation of the national strategy. Among other requirements, the implementation plan must establish, for federal broadband programs that are not technologically neutral (i.e., programs\u00a0that involve a preference for certain broadband technologies), a ceiling on the amount of funding that may be awarded to support the provision of broadband service to a single location.\u00a0</p><p>The bill also requires executive branch agencies to identify and address factors that contribute to delays in their review of applications for easements, rights-of-way, or leases related to communications infrastructure projects on federal property. (Under current law, agencies are generally required to act on such applications within 270 days.) Agencies must also establish methods to alert employees when the agency is at risk of failing to meet the 270-day deadline with respect to a particular application.\u00a0</p><p>Finally, the bill lowers the cost threshold for certain broadband infrastructure projects to qualify as <em>covered projects</em> under the Fixing America's Surface Transportation (FAST) Act from $200 million to $5 million. Such projects qualify for expedited federal environmental review.</p>",
      "updateDate": "2025-07-16",
      "versionCode": "id119s323"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s323is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s323rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "PLAN for Broadband Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-23T06:53:30Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Proper Leadership to Align Networks for Broadband Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-23T06:53:30Z"
    },
    {
      "title": "PLAN for Broadband Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PLAN for Broadband Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Proper Leadership to Align Networks for Broadband Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Assistant Secretary of Commerce for Communications and Information to develop a National Strategy to Synchronize Federal Broadband Programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:04:01Z"
    }
  ]
}
```
