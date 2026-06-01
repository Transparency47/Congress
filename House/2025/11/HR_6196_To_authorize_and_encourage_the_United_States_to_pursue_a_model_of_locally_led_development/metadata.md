# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6196?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6196
- Title: Locally Led Development and Humanitarian Response Act
- Congress: 119
- Bill type: HR
- Bill number: 6196
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-05-19T18:05:32Z
- Update date including text: 2026-05-19T18:05:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 36 - 10.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 36 - 10.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6196",
    "number": "6196",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "J000305",
        "district": "51",
        "firstName": "Sara",
        "fullName": "Rep. Jacobs, Sara [D-CA-51]",
        "lastName": "Jacobs",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Locally Led Development and Humanitarian Response Act",
    "type": "HR",
    "updateDate": "2026-05-19T18:05:32Z",
    "updateDateIncludingText": "2026-05-19T18:05:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 36 - 10.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
        "item": [
          {
            "date": "2026-03-26T16:20:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-20T15:01:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6196ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6196\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Ms. Jacobs (for herself and Mrs. Kim ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo authorize and encourage the United States to pursue a model of locally led development and humanitarian response and expand engagement with local actors and increase its local partner base.\n#### 1. Short title\nThis Act may be cited as the Locally Led Development and Humanitarian Response Act .\n#### 2. Purpose\nThe purpose of this Act is to encourage the United States to pursue a model of locally led development and humanitarian response and expand engagement and partnership with local actors.\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nlocally led development and humanitarian response is linked to more efficient and sustainable development and humanitarian outcomes, and is vital to building long-term self-reliance;\n**(2)**\nover multiple Administrations, the United States Government has sought to achieve greater development outcomes through stronger local partnerships, including through Country Ownership , The Journey to Self-Reliance , and Locally Led Development ;\n**(3)**\nthe relevant foreign assistance agency should increase the proportion of direct funding to local entities, including by increasing the amount of development and humanitarian assistance to such entities;\n**(4)**\nthe relevant foreign assistance agency should ensure its programming enables local communities to exercise leadership over priorities, project design, implementation, and measuring and evaluating results of such programs;\n**(5)**\nthe relevant foreign assistance agency should ensure most awards, requests for proposals, and requests for applications outline expectations for implementers to elevate local leadership and hold implementers to account for elevating local leadership;\n**(6)**\nworking with local partners requires more time, staffing, and flexibility of resources than traditional partners, including extended availability of funds and additional staff resources; and\n**(7)**\nincreased flexibility is critical to respond to local priorities and leverage local capacities, including with respect to staffing, availability of funds, program design, and acquisition and assistance processes, among other areas.\n#### 4. Working with local partners\n##### (a) In general\nTo the extent feasible and appropriate, the head of the relevant foreign assistance agency should localize the development and humanitarian assistance partner base by considering\u2014\n**(1)**\nsupporting and funding existing effective local projects and initiatives;\n**(2)**\nsimplifying and increasing access to United States foreign assistance resources for local partners in humanitarian and development sectors, including local partners who have relations, agency, or power structures in place that have produced, or can produce, strong trust, accountability, and legitimacy in the communities or networks such partners work in;\n**(3)**\nsetting realistic goals and timelines for sunsetting assistance and adhering to existing agreement totals and timelines to incentivize self-reliance and encourage exit plans with appropriate notice;\n**(4)**\nexploring offering matching grants and in-kind contributions to ensure that United States Government investments in local partners are helping generate new resources of their own from other donors;\n**(5)**\nexploring government-to-government partnerships with adequate guardrails and oversight, in consultation with local civil society, with select countries where feasible and practical to enhance foreign governments\u2019 ability to deliver good governance, service delivery, and public goods that benefit local communities;\n**(6)**\nexploring other types of funding modalities and types of partnerships with local and national actors, including support for pooled funding mechanisms and unsolicited projects;\n**(7)**\ndiversifying award types to streamline performance requirements and working with the Office of Management and Budget to address threshold constraints that pose a barrier to effectively supporting local partners;\n**(8)**\nensuring staff of the relevant foreign assistance agency is able and encouraged to conduct regular consultation with local partners in local languages of the host countries relating to policies and programs, including making available solicitations for acquisitions and assistance and accepting submissions in local languages, video format, or verbal presentations, including by\u2014\n**(A)**\ninvesting in translation services;\n**(B)**\nhosting workshop-based engagements; and\n**(C)**\nadvertising solicitations in local trade publications, local media including newspapers and radio, local community centers, and local online forums;\n**(9)**\nallowing and promoting multi-year, flexible, tiered and milestone-based funding for new programs and to bring successful programs to scale;\n**(10)**\nutilizing other transaction authority through innovation incentive awards for local and national actors;\n**(11)**\nsupporting consistent and unimpeded access to full cost recovery for local partners implementing United States foreign assistance activities;\n**(12)**\nundertaking outreach campaigns and engaging with local actors, formally and informally, to raise awareness about opportunities, as well as how to apply for and manage awards in compliance with applicable Federal regulations and the relevant foreign assistance agency policies, and ensuring such engagement is accessible to all entities, including unregistered and informal organizations;\n**(13)**\nstrengthening oversight of capacity strengthening components of awards to ensure United States and international awardees are making good-faith efforts to strengthen local organizations\u2019 capacities, including independent and external evaluations to evaluate the mentorship process and regular feedback loops;\n**(14)**\nensuring there are sufficient acquisition and assistance personnel;\n**(15)**\nsoliciting feedback on and updating, as necessary, performance evaluation criteria to create greater workforce incentives for the relevant foreign assistance agency personnel to champion locally led development;\n**(16)**\naddressing internal delays and recipient organization issues that result in the required extension of provisional Negotiated Indirect Cost Rates (NICRAs);\n**(17)**\nconducting seminars and providing documentation in local languages on NICRA, the de minimis indirect cost rate, and other options for indirect cost recovery relevant to the award type; and\n**(18)**\nensuring that acquisition and assistance personnel communicate to awardees who do not submit for a NICRA that they are eligible for the de minimis indirect cost rate.\n#### 5. Institutionalization of actions described in section 4\nNot later than 180 days after the date of the enactment of this Act, the head of the relevant foreign assistance agency shall initiate policy actions, including rulemaking if necessary, to institutionalize the actions described in section 4 to the extent appropriate and feasible within all relevant foreign assistance agency internal rules and regulations, including the Foreign Affairs Manual, the Foreign Affairs Handbook, and the Department of State Acquisition Regulation, as well as other relevant strategies and policies.\n#### 6. Authority to accept applications, proposals, and contracting agreements in local languages and local language support\n##### (a) In general\nNotwithstanding any other provision of law, the relevant foreign assistance agency is authorized to accept applications or proposals in languages other than English if such acceptance eases the burden of a local actor working with such agency and such agency is able to effectively evaluate such applications or proposals.\n##### (b) Local language support\n**(1) In general**\nThe head of the relevant foreign assistance agency shall conduct an assessment of options to enable such agency to utilize local languages to support local partners with award solicitations, proposals and applications, evaluations, management, close out, and other types of partnerships, including advising local partners on applicable United States regulations and the relevant foreign assistance agency policies and local country rules and regulations common in such activities.\n**(2) Report**\nNot later than 1 year after the date of the enactment of this Act, the head of the relevant foreign assistance agency shall submit to Congress a report on the assessment described in this subsection.\n#### 7. Modifications relating to the code of Federal regulations and other requirements\n##### (a) Increase in the de minimis indirect cost\nThe head of the relevant foreign assistance agency is authorized to\u2014\n**(1)**\nincrease the de minimis indirect cost rate provided for in section 200.414 of title 2, Code of Federal Regulations, or any successor regulations, by 5 percentage points for local partners receiving assistance awards from the agency; and\n**(2)**\nestablish a de minimis indirect cost rate at the same rate provided for in paragraph (1) for acquisitions awarded under title 48 of the Code of Federal Regulations to local partners, and to increase this threshold further should subsequent Office of Management and Budget regulations recommend doing so.\n##### (b) Exemption for local entities\nThe head of the relevant foreign assistance agency is authorized to exempt local partners, as needed, from the reporting requirements of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6106 note; Public Law 109\u2013282 ) to allow for a 180-day delay in obtaining a unique entity identifier and registration in the System for Award Management. This delay shall be no later than 30 days prior to the end of the award\u2019s period of performance.\n##### (c) Local competition authority\nNotwithstanding any other provision of law, the head of the relevant foreign assistance agency (or their designees) may award contracts and other acquisition instruments in which competition is limited to local entities if doing so would result in cost savings, strengthen local capacity, or enable the agency to deliver programs or activities more sustainably or quickly than if competition were not so limited. Such authority may not be used to make acquisition awards in excess of $25,000,000 and shall not exceed more than 10 percent of the amounts appropriated to the relevant foreign assistance agency each fiscal year.\n##### (d) Use of national or international generally accepted accounting principles\nThe head of the relevant foreign assistance agency, in consultation with the Administrator of the General Services Administration, the Secretary of Defense, and the Administrator of the National Aeronautics and Space Administration, is authorized to allow foreign entities to use national or international generally accepted accounting principles instead of United States Generally Accepted Accounting Principles (GAAP) for contracts or grants awarded under the chapter 7 of title 48, Code of Federal Regulations or chapter 7 of title 2, Code of Federal Regulations.\n#### 8. Review of locally-led development in public international organizations\nNot later than 1 year after the date of the enactment of this Act, the head of the relevant foreign assistance agency shall submit to the appropriate congressional committees a review of public international organizations\u2019 support for locally-led development, to include the following elements:\n**(1)**\nAn assessment of how such organizations\u2019 approaches and financing structures support locally-led development and humanitarian response.\n**(2)**\nAn action plan for how the United States will use its position in such organizations to encourage greater focus on locally-led approaches.\n#### 9. Annual report\nNot later than 1 year after the end of the first fiscal year following the date of the enactment of this Act, and annually thereafter, the head of the relevant foreign assistance agency shall submit to the appropriate congressional committees and publish on the agency\u2019s website a report on the agency\u2019s progress to advance locally led development and humanitarian response, to include the following elements:\n**(1)**\nThe amount of funding implemented directly and indirectly by local partners, including to local and national nonprofit organizations, local and national governments, and local and national private sector entities, in the previous fiscal year, including all development and humanitarian assistance programs.\n**(2)**\nAn assessment of how the agency is enabling more local leadership of foreign assistance programs, including recipients of direct funding, subrecipients and subcontractors to an international implementing partner, participants in an agency program, or members of a community affected by such programming.\n**(3)**\nAn assessment of how the relevant foreign assistance agency is using new authorities granted in sections 6 and 7 and an assessment of the impact of these authorities on such agency\u2019s ability to work with local partners and communities.\n**(4)**\nAn assessment of how many organizations with a Negotiated Indirect Cost Rate (NICRA) cognizant to the relevant foreign assistance agency are utilizing provisional NICRAs for over 48 months without a final NICRA and steps that such agency can take to reduce the extension of provisional NICRAs beyond 12 months.\n#### 10. Report on contracting officers\nNot later than 180 days after the enactment of this Act, the head of the relevant foreign assistance agency shall provide a report to the appropriate congressional committees on the recruitment and retention of contracting officers and grant officers at such agency and recommendations to improve contracting/agreement officer recruitment and retention.\n#### 11. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs and the Committee on Appropriations of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations and the Committee on Appropriations of the Senate.\n**(2) Local partner**\nThe term local partner means\u2014\n**(A)**\nan individual who is a citizen or lawfully admitted permanent resident of and have his or her principal place of business in the country or region receiving United States foreign assistance with which the individual is or may become involved;\n**(B)**\na sole proprietorship that is owned by such an individual that meets the requirements of subparagraph (A); or\n**(C)**\nan entity that\u2014\n**(i)**\nis incorporated or legally organized under the laws of, and have its principal place of business in, the country served by the program with which the entity is involved or in a country within the same region as the program with which the entity is involved;\n**(ii)**\ndetermines its own autonomous leadership and governance structures, sets its own strategic direction, priorities, and programmatic focus, and makes independent financial decisions separately from an international organization;\n**(iii)**\nif it has a Board of Directors, has 51 percent or more board directors who are citizens or lawfully permanent residents of such country or a country within the same region; and\n**(iv)**\nif it is a corporation, is 75 percent beneficially owned at the time of application by individuals who are citizens or lawfully admitted permanent residents of that same country.\n**(3) Relevant foreign assistance agency**\nThe term relevant foreign assistance agency means the department or agency designated as primarily responsible for implementing the United States foreign assistance under part I of the Foreign Assistance Act of 1961.",
      "versionDate": "2025-11-20",
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
            "name": "Accounting and auditing",
            "updateDate": "2026-05-04T20:11:28Z"
          },
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-05-04T20:11:37Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2026-05-04T20:12:26Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-04T20:11:56Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2026-05-04T20:12:03Z"
          },
          {
            "name": "Foreign language and bilingual programs",
            "updateDate": "2026-05-04T20:12:11Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2026-05-04T20:11:48Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2026-05-04T20:12:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2026-01-23T14:59:59Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6196ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize and encourage the United States to pursue a model of locally-led development and humanitarian response and expand engagement with local actors and increase its local partner base.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-23T03:59:05Z"
    },
    {
      "title": "Locally Led Development and Humanitarian Response Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-23T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Locally Led Development and Humanitarian Response Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-23T03:53:16Z"
    }
  ]
}
```
