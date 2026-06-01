# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3315?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3315
- Title: Health Care Cybersecurity and Resiliency Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3315
- Origin chamber: Senate
- Introduced date: 2025-12-02
- Update date: 2026-04-20T12:50:21Z
- Update date including text: 2026-04-20T12:50:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in Senate
- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-02-26 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-03-23 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2026-03-23 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2026-03-23 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 365.
- Latest action: 2025-12-02: Introduced in Senate

## Actions

- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-02-26 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-03-23 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2026-03-23 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2026-03-23 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 365.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3315",
    "number": "3315",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Health Care Cybersecurity and Resiliency Act of 2026",
    "type": "S",
    "updateDate": "2026-04-20T12:50:21Z",
    "updateDateIncludingText": "2026-04-20T12:50:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-23",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 365.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-03-23",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-03-23",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-26",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-02",
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
            "date": "2026-03-23T20:45:05Z",
            "name": "Reported By"
          },
          {
            "date": "2026-02-26T15:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-02T22:13:52Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NH"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "TX"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3315is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3315\nIN THE SENATE OF THE UNITED STATES\nDecember 2, 2025 Mr. Cassidy (for himself, Ms. Hassan , Mr. Cornyn , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require the Secretary of Health and Human Services and the Director of the Cybersecurity and Infrastructure Security Agency to coordinate to improve cybersecurity in the health care and public health sectors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Health Care Cybersecurity and Resiliency Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Agency**\nThe term Agency means the Cybersecurity and Infrastructure Security Agency.\n**(2) Cybersecurity incident**\nThe term cybersecurity incident has the meaning given the term incident in section 3552 of title 44, United States Code.\n**(3) Cybersecurity State Coordinator**\nThe term Cybersecurity State Coordinator means a Cybersecurity State Coordinator appointed under section 2217(a) of the Homeland Security Act of 2002 ( 6 U.S.C. 665c(a) ).\n**(4) Director**\nThe term Director means the Director of the Agency.\n**(5) Healthcare and Public Health Sector**\nThe term Healthcare and Public Health Sector means the Healthcare and Public Health sector, as identified in Presidential Policy Directive 21 (February 12, 2013; relating to critical infrastructure security and resilience).\n**(6) Information Sharing and Analysis Organization**\nThe term Information Sharing and Analysis Organization has the meaning given such term in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ).\n**(7) Information system**\nThe term information system has the meaning given such term in section 102 of the Cybersecurity Information Sharing Act of 2015 ( 6 U.S.C. 1501 ).\n**(8) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n#### 3. Department coordination with the Agency\n##### (a) In general\nThe Secretary and the Director shall coordinate, including by entering into a cooperative agreement, as appropriate, to improve cybersecurity in the Healthcare and Public Health Sector.\n##### (b) Assistance\n**(1) In general**\nThe Secretary shall coordinate with the Director to make resources available to entities that are receiving information shared through programs managed by the Director or the Secretary, including Information Sharing and Analysis Organizations, information sharing and analysis centers, and non-Federal entities.\n**(2) Scope**\nThe coordination under paragraph (1) shall include\u2014\n**(A)**\ndeveloping products specific to the needs of Healthcare and Public Health Sector entities; and\n**(B)**\nsharing information relating to cyber threat indicators and appropriate defensive measures.\n#### 4. Clarifying cybersecurity responsibilities at the Department of Health and Human Services\nPart A of title III of the Public Health Service Act ( 42 U.S.C. 241 et seq. ) is amended by adding at the end the following:\n310C. Oversight of cybersecurity activities The Secretary, acting through the Assistant Secretary for Preparedness and Response, in coordination with the Director of the Cybersecurity and Infrastructure Security Agency pursuant to section 2218 of the Homeland Security Act of 2002, shall lead oversight and coordination of activities within the Department of Health and Human Services to support cybersecurity resiliency within the Healthcare and Public Health Sector (as defined in section 2 of the Health Care Cybersecurity and Resiliency Act of 2025 ), including coordination and communication with other public and private entities related to preparedness for, and responses to, cybersecurity incidents, consistent with applicable provisions of this Act, other applicable laws, and Presidential Policy Directive 21 (February 12, 2013; relating to critical infrastructure security and resilience). .\n#### 5. Cybersecurity incident response plan\nSection 405 of the Cybersecurity Act of 2015 ( 6 U.S.C. 1533 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (4)\u2014\n**(i)**\nin the paragraph heading, by inserting information system; after Federal entity; ; and\n**(ii)**\nby inserting information system , after Federal entity , ;\n**(B)**\nby redesignating paragraphs (4) through (7) as paragraphs (6) through (9), respectively; and\n**(C)**\nby inserting after paragraph (3) the following:\n(4) Cybersecurity incident The term cybersecurity incident has the meaning given the term incident in section 3552 of title 44, United States Code. (5) Cybersecurity risk The term cybersecurity risk has the meaning given such term in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ). ; and\n**(2)**\nin subsection (d), by adding at the end the following:\n(4) Plan (A) In general Not later than 1 year after the date of enactment of the Health Care Cybersecurity and Resiliency Act of 2025 , the Secretary shall develop and implement a cybersecurity incident response plan to inform applicable personnel within the Department of Health and Human Services of processes and protocols to prepare for, and respond to, cybersecurity incidents involving information, including hardware, software, databases, and networks, used or maintained by, or on behalf of, the Department, including strategies\u2014 (i) to assess cybersecurity risks; (ii) to prevent cybersecurity incidents; (iii) to detect and identify cybersecurity incidents; (iv) to minimize damage in the event of a cybersecurity incident; (v) to protect data; and (vi) to recover from any cybersecurity incidents expeditiously. (B) Consultation In developing the plan under subparagraph (A), the Secretary shall consult with the Director of the Cybersecurity and Infrastructure Security Agency, the Director of the Office of Management and Budget, and the Director of the National Institute of Standards and Technology, and relevant experts, as appropriate. (C) Report Not later than 60 days before the date on which the Secretary begins implementing the plan under subparagraph (A), the Secretary shall submit to the Committee on Health, Education, Labor, and Pensions and the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Energy and Commerce, the Committee on Oversight and Reform, and the Committee on Homeland Security of the House of Representatives a report that describes such plan. .\n#### 6. Breach reporting portal\n##### (a) Updates to breach reporting portal\nSection 13402 of the HITECH Act ( 42 U.S.C. 17932 ) is amended by adding at the end the following:\n(k) Updates to regulations Not later than 1 year after the date of enactment of the Health Care Cybersecurity and Resiliency Act of 2025 , the Secretary shall update the regulations promulgated pursuant to subsection (j) to require that information required to be publicly displayed in the breach reporting portal established pursuant to this section includes\u2014 (1) information on any corrective action taken against a covered entity that provided notification of a breach under this section; (2) information on whether and to what extent, as appropriate, recognized security practices (as defined in section 13412(b)(1)) were considered in the investigation of such a breach; and (3) such additional information about such a breach as the Secretary may require. .\n#### 7. Clarifying breach reporting obligations\nSection 13402(f) of the HITECH Act ( 42 U.S.C. 17932(f) ) is amended by adding at the end the following:\n(6) The number of individuals affected by the breach. .\n#### 8. Enhancing recognition of security practices\n##### (a) Recognized security practices\nSection 13412(b)(1) of the HITECH Act ( 42 U.S.C. 17941(b)(1) ) is amended, in the first sentence, by inserting , investments, after other programs .\n##### (b) Guidance\nNot later than 1 year after the date of enactment of this Act, the Secretary shall issue guidance on the implementation of section 13412 of the HITECH Act ( 42 U.S.C. 17941 ), which shall include\u2014\n**(1)**\nrecognized security practices (as defined in subsection (b)(1) of such section) that the Secretary may consider when determining fines under such section;\n**(2)**\nthe extent to which such recognized security practices should be in place for consideration by the Secretary; and\n**(3)**\nprocedural requirements or information that shall be submitted by a covered entity or business associate (as such terms are defined in section 13400 of the HITECH Act ( 42 U.S.C. 17921 )) to the Secretary for consideration.\n##### (c) Annual report\nNot later than 2 years after the date of enactment of this Act, and annually thereafter, the Secretary shall include in the annual report required under section 13424(a) of the HITECH Act ( 42 U.S.C. 17953(a) ) information on implementation of section 13412 of such Act ( 42 U.S.C. 17941 ), including an accounting of every case in which the Secretary considered recognized security practices (as defined in subsection (b)(1) of such section) when effectuating audits and assessing fines under such section.\n#### 9. Required cybersecurity standards\n##### (a) In general\nThe Secretary shall update the privacy, security, and breach notification regulations under parts 160 and 164 of title 45, Code of Federal Regulations (or any successor regulation) to require covered entities and business associates to adopt the following cybersecurity practices:\n**(1)**\nMultifactor authentication, or a successor technology, for access to any information systems that may include protected health information.\n**(2)**\nSafeguards to encrypt protected health information.\n**(3)**\nRequirements to conduct audits, including penetration testing, to maintain the protections of information systems.\n**(4)**\nOther minimum cybersecurity standards, as determined by the Secretary, in consultation with private sector entities, based on landscape analysis of emerging and existing cybersecurity vulnerabilities and consensus-based best practices.\n##### (b) Effective dates\nThe Secretary shall specify in the regulations the effective date for each of the new requirements under the regulations updated in accordance with subsection (a). Each such effective date shall provide reasonable time for the entities subject to the requirement to come into compliance.\n#### 10. Guidance on rural cybersecurity readiness\nSection 405(d) of the Cybersecurity Act of 2015 ( 6 U.S.C. 1533(d) ) (as amended by section 5(2)) is amended by adding at the end the following:\n(5) Rural cybersecurity guidance (A) Definition of rural In this paragraph, the term rural has the meaning given such term by the Health Resources and Services Administration. (B) Guidance on rural cybersecurity readiness Not later than 1 year after the date of enactment of the Health Care Cybersecurity and Resiliency Act of 2025 , the Secretary shall issue guidance to rural entities on best practices to improve cyber readiness, including strategies\u2014 (i) to improve cyber infrastructure, including any technical safeguards to mitigate cybersecurity risk; (ii) to integrate best practices issued by the Secretary to improve cybersecurity preparedness; (iii) to improve employee preparation to mitigate any cybersecurity risks, including existing public-private programs to support educational initiatives; and (iv) to implement policies to facilitate mandatory cybersecurity incident reporting requirements under law. (C) GAO study and report (i) In general Not later than 3 years after the date of enactment of the Health Care Cybersecurity and Resiliency Act of 2025 , the Comptroller General of the United States shall conduct, and submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that describes the results of, a study to examine how rural entities have implemented the recommendations included in the guidance under subparagraph (B). (ii) Requirements The study under clause (i) shall assess\u2014 (I) how rural entities have implemented any technical safeguards and any challenges faced by such rural entities in areas for which safeguards were not implemented; (II) steps to further support cyber resilience for rural entities; (III) areas to improve coordination between Federal agencies, including for the purposes of required cyber reporting; and (IV) any opportunities to support public-private collaboration in the area of cyber readiness. .\n#### 11. Grants to enhance cybersecurity in the health and public health sectors\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g et seq. ) is amended by adding at the end the following:\n399V\u20138. Grants (a) In general The Secretary may award grants to eligible entities for the adoption and use of cybersecurity best practices. (b) Eligible entity To be eligible to receive a grant under subsection (a) an entity shall be\u2014 (1) a public or nonprofit private health center (including a Federally qualified health center (as defined in section 1861(aa)(4) of the Social Security Act)); (2) a health facility operated by or pursuant to a contract with the Indian Health Service; (3) a hospital; (4) a cancer center; (5) a rural health clinic; (6) an academic health center; or (7) a nonprofit entity that enters into a partnership or coordinates referrals with an entity described in any of paragraphs (1) through (6). (c) Use of funds In adopting and using cybersecurity best practices pursuant to a grant under subsection (a), an eligible entity may use grant funds\u2014 (1) to hire and train personnel in such cybersecurity best practices; (2) to update electronic data systems, such as by migrating to cloud based platforms; (3) to join and participate in health cybersecurity threat information sharing organizations; (4) to reduce the use of legacy systems; and (5) to contract with third parties to assist with the activities described in paragraphs (1) through (5). (d) Grant period The Secretary may award a grant under this section for a period of not more than 3 years. (e) Application An eligible entity seeking a grant under subsection (a) shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require including, at a minimum a description of how the eligible entity will establish baseline measures and benchmarks that meet the Secretary\u2019s requirements to evaluate program outcomes. (f) Authorization of appropriations There are authorized to be appropriated to carry out this section such sums as may be necessary for each of fiscal years 2025 through 2030. .\n#### 12. Healthcare cybersecurity workforce\n##### (a) Training for healthcare experts\nThe Secretary, in coordination with the Cybersecurity State Coordinators of the Agency and private sector health care experts, as appropriate, shall provide training to Healthcare and Public Health Sector asset owners and operators on\u2014\n**(1)**\ncybersecurity risks to information systems within the Healthcare and Public Health Sector; and\n**(2)**\nways to mitigate the risks to information systems in the Healthcare and Public Health Sector.\n##### (b) Cross-Agency educational tools\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary, acting through the Administrator of the Health Resources and Services Administration, in coordination with the Agency, shall develop a strategic plan to support growing the cybersecurity workforce for health care entities.\n**(2) Inclusions**\nThe strategic plan under paragraph (1) shall include\u2014\n**(A)**\nrecommendations for existing educational programs that can be used to support cybersecurity training;\n**(B)**\ndissemination and development of educational materials on how to improve cybersecurity resilience;\n**(C)**\ndevelopment of best practices to train the health care workforce on cybersecurity best practices; and\n**(D)**\nopportunities for public-private collaboration to strengthen the cybersecurity workforce.",
      "versionDate": "2025-12-02",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3315rs.xml",
      "text": "II\nCalendar No. 365\n119th CONGRESS\n2d Session\nS. 3315\nIN THE SENATE OF THE UNITED STATES\nDecember 2, 2025 Mr. Cassidy (for himself, Ms. Hassan , Mr. Cornyn , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nMarch 23, 2026 Reported by Mr. Cassidy , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require the Secretary of Health and Human Services and the Director of the Cybersecurity and Infrastructure Security Agency to coordinate to improve cybersecurity in the health care and public health sectors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Health Care Cybersecurity and Resiliency Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Agency**\nThe term Agency means the Cybersecurity and Infrastructure Security Agency.\n**(2) Cybersecurity incident**\nThe term cybersecurity incident has the meaning given the term incident in section 3552 of title 44, United States Code.\n**(3) Cybersecurity State Coordinator**\nThe term Cybersecurity State Coordinator means a Cybersecurity State Coordinator appointed under section 2217(a) of the Homeland Security Act of 2002 ( 6 U.S.C. 665c(a) ).\n**(4) Director**\nThe term Director means the Director of the Agency.\n**(5) Healthcare and Public Health Sector**\nThe term Healthcare and Public Health Sector means the Healthcare and Public Health sector, as identified in Presidential Policy Directive 21 (February 12, 2013; relating to critical infrastructure security and resilience).\n**(6) Information Sharing and Analysis Organization**\nThe term Information Sharing and Analysis Organization has the meaning given such term in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ).\n**(7) Information system**\nThe term information system has the meaning given such term in section 102 of the Cybersecurity Information Sharing Act of 2015 ( 6 U.S.C. 1501 ).\n**(8) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n#### 3. Department coordination with the Agency\n##### (a) In general\nThe Secretary and the Director shall coordinate, including by entering into a cooperative agreement, as appropriate, to improve cybersecurity in the Healthcare and Public Health Sector.\n##### (b) Assistance\n**(1) In general**\nThe Secretary shall coordinate with the Director to make resources available to entities that are receiving information shared through programs managed by the Director or the Secretary, including Information Sharing and Analysis Organizations, information sharing and analysis centers, and non-Federal entities.\n**(2) Scope**\nThe coordination under paragraph (1) shall include\u2014\n**(A)**\ndeveloping products specific to the needs of Healthcare and Public Health Sector entities; and\n**(B)**\nsharing information relating to cyber threat indicators and appropriate defensive measures.\n#### 4. Clarifying cybersecurity responsibilities at the Department of Health and Human Services\nPart A of title III of the Public Health Service Act ( 42 U.S.C. 241 et seq. ) is amended by adding at the end the following:\n310C. Oversight of cybersecurity activities The Secretary, acting through the Assistant Secretary for Preparedness and Response, in coordination with the Director of the Cybersecurity and Infrastructure Security Agency pursuant to section 2218 of the Homeland Security Act of 2002, shall lead oversight and coordination of activities within the Department of Health and Human Services to support cybersecurity resiliency within the Healthcare and Public Health Sector (as defined in section 2 of the Health Care Cybersecurity and Resiliency Act of 2025 ), including coordination and communication with other public and private entities related to preparedness for, and responses to, cybersecurity incidents, consistent with applicable provisions of this Act, other applicable laws, and Presidential Policy Directive 21 (February 12, 2013; relating to critical infrastructure security and resilience). .\n#### 5. Cybersecurity incident response plan\nSection 405 of the Cybersecurity Act of 2015 ( 6 U.S.C. 1533 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (4)\u2014\n**(i)**\nin the paragraph heading, by inserting information system; after Federal entity; ; and\n**(ii)**\nby inserting information system , after Federal entity , ;\n**(B)**\nby redesignating paragraphs (4) through (7) as paragraphs (6) through (9), respectively; and\n**(C)**\nby inserting after paragraph (3) the following:\n(4) Cybersecurity incident The term cybersecurity incident has the meaning given the term incident in section 3552 of title 44, United States Code. (5) Cybersecurity risk The term cybersecurity risk has the meaning given such term in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ). ; and\n**(2)**\nin subsection (d), by adding at the end the following:\n(4) Plan (A) In general Not later than 1 year after the date of enactment of the Health Care Cybersecurity and Resiliency Act of 2025 , the Secretary shall develop and implement a cybersecurity incident response plan to inform applicable personnel within the Department of Health and Human Services of processes and protocols to prepare for, and respond to, cybersecurity incidents involving information, including hardware, software, databases, and networks, used or maintained by, or on behalf of, the Department, including strategies\u2014 (i) to assess cybersecurity risks; (ii) to prevent cybersecurity incidents; (iii) to detect and identify cybersecurity incidents; (iv) to minimize damage in the event of a cybersecurity incident; (v) to protect data; and (vi) to recover from any cybersecurity incidents expeditiously. (B) Consultation In developing the plan under subparagraph (A), the Secretary shall consult with the Director of the Cybersecurity and Infrastructure Security Agency, the Director of the Office of Management and Budget, and the Director of the National Institute of Standards and Technology, and relevant experts, as appropriate. (C) Report Not later than 60 days before the date on which the Secretary begins implementing the plan under subparagraph (A), the Secretary shall submit to the Committee on Health, Education, Labor, and Pensions and the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Energy and Commerce, the Committee on Oversight and Reform, and the Committee on Homeland Security of the House of Representatives a report that describes such plan. .\n#### 6. Breach reporting portal\n##### (a) Updates to breach reporting portal\nSection 13402 of the HITECH Act ( 42 U.S.C. 17932 ) is amended by adding at the end the following:\n(k) Updates to regulations Not later than 1 year after the date of enactment of the Health Care Cybersecurity and Resiliency Act of 2025 , the Secretary shall update the regulations promulgated pursuant to subsection (j) to require that information required to be publicly displayed in the breach reporting portal established pursuant to this section includes\u2014 (1) information on any corrective action taken against a covered entity that provided notification of a breach under this section; (2) information on whether and to what extent, as appropriate, recognized security practices (as defined in section 13412(b)(1)) were considered in the investigation of such a breach; and (3) such additional information about such a breach as the Secretary may require. .\n#### 7. Clarifying breach reporting obligations\nSection 13402(f) of the HITECH Act ( 42 U.S.C. 17932(f) ) is amended by adding at the end the following:\n(6) The number of individuals affected by the breach. .\n#### 8. Enhancing recognition of security practices\n##### (a) Recognized security practices\nSection 13412(b)(1) of the HITECH Act ( 42 U.S.C. 17941(b)(1) ) is amended, in the first sentence, by inserting , investments, after other programs .\n##### (b) Guidance\nNot later than 1 year after the date of enactment of this Act, the Secretary shall issue guidance on the implementation of section 13412 of the HITECH Act ( 42 U.S.C. 17941 ), which shall include\u2014\n**(1)**\nrecognized security practices (as defined in subsection (b)(1) of such section) that the Secretary may consider when determining fines under such section;\n**(2)**\nthe extent to which such recognized security practices should be in place for consideration by the Secretary; and\n**(3)**\nprocedural requirements or information that shall be submitted by a covered entity or business associate (as such terms are defined in section 13400 of the HITECH Act ( 42 U.S.C. 17921 )) to the Secretary for consideration.\n##### (c) Annual report\nNot later than 2 years after the date of enactment of this Act, and annually thereafter, the Secretary shall include in the annual report required under section 13424(a) of the HITECH Act ( 42 U.S.C. 17953(a) ) information on implementation of section 13412 of such Act ( 42 U.S.C. 17941 ), including an accounting of every case in which the Secretary considered recognized security practices (as defined in subsection (b)(1) of such section) when effectuating audits and assessing fines under such section.\n#### 9. Required cybersecurity standards\n##### (a) In general\nThe Secretary shall update the privacy, security, and breach notification regulations under parts 160 and 164 of title 45, Code of Federal Regulations (or any successor regulation) to require covered entities and business associates to adopt the following cybersecurity practices:\n**(1)**\nMultifactor authentication, or a successor technology, for access to any information systems that may include protected health information.\n**(2)**\nSafeguards to encrypt protected health information.\n**(3)**\nRequirements to conduct audits, including penetration testing, to maintain the protections of information systems.\n**(4)**\nOther minimum cybersecurity standards, as determined by the Secretary, in consultation with private sector entities, based on landscape analysis of emerging and existing cybersecurity vulnerabilities and consensus-based best practices.\n##### (b) Effective dates\nThe Secretary shall specify in the regulations the effective date for each of the new requirements under the regulations updated in accordance with subsection (a). Each such effective date shall provide reasonable time for the entities subject to the requirement to come into compliance.\n#### 10. Guidance on rural cybersecurity readiness\nSection 405(d) of the Cybersecurity Act of 2015 ( 6 U.S.C. 1533(d) ) (as amended by section 5(2)) is amended by adding at the end the following:\n(5) Rural cybersecurity guidance (A) Definition of rural In this paragraph, the term rural has the meaning given such term by the Health Resources and Services Administration. (B) Guidance on rural cybersecurity readiness Not later than 1 year after the date of enactment of the Health Care Cybersecurity and Resiliency Act of 2025 , the Secretary shall issue guidance to rural entities on best practices to improve cyber readiness, including strategies\u2014 (i) to improve cyber infrastructure, including any technical safeguards to mitigate cybersecurity risk; (ii) to integrate best practices issued by the Secretary to improve cybersecurity preparedness; (iii) to improve employee preparation to mitigate any cybersecurity risks, including existing public-private programs to support educational initiatives; and (iv) to implement policies to facilitate mandatory cybersecurity incident reporting requirements under law. (C) GAO study and report (i) In general Not later than 3 years after the date of enactment of the Health Care Cybersecurity and Resiliency Act of 2025 , the Comptroller General of the United States shall conduct, and submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that describes the results of, a study to examine how rural entities have implemented the recommendations included in the guidance under subparagraph (B). (ii) Requirements The study under clause (i) shall assess\u2014 (I) how rural entities have implemented any technical safeguards and any challenges faced by such rural entities in areas for which safeguards were not implemented; (II) steps to further support cyber resilience for rural entities; (III) areas to improve coordination between Federal agencies, including for the purposes of required cyber reporting; and (IV) any opportunities to support public-private collaboration in the area of cyber readiness. .\n#### 11. Grants to enhance cybersecurity in the health and public health sectors\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g et seq. ) is amended by adding at the end the following:\n399V\u20138. Grants (a) In general The Secretary may award grants to eligible entities for the adoption and use of cybersecurity best practices. (b) Eligible entity To be eligible to receive a grant under subsection (a) an entity shall be\u2014 (1) a public or nonprofit private health center (including a Federally qualified health center (as defined in section 1861(aa)(4) of the Social Security Act)); (2) a health facility operated by or pursuant to a contract with the Indian Health Service; (3) a hospital; (4) a cancer center; (5) a rural health clinic; (6) an academic health center; or (7) a nonprofit entity that enters into a partnership or coordinates referrals with an entity described in any of paragraphs (1) through (6). (c) Use of funds In adopting and using cybersecurity best practices pursuant to a grant under subsection (a), an eligible entity may use grant funds\u2014 (1) to hire and train personnel in such cybersecurity best practices; (2) to update electronic data systems, such as by migrating to cloud based platforms; (3) to join and participate in health cybersecurity threat information sharing organizations; (4) to reduce the use of legacy systems; and (5) to contract with third parties to assist with the activities described in paragraphs (1) through (5). (d) Grant period The Secretary may award a grant under this section for a period of not more than 3 years. (e) Application An eligible entity seeking a grant under subsection (a) shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require including, at a minimum a description of how the eligible entity will establish baseline measures and benchmarks that meet the Secretary\u2019s requirements to evaluate program outcomes. (f) Authorization of appropriations There are authorized to be appropriated to carry out this section such sums as may be necessary for each of fiscal years 2025 through 2030. .\n#### 12. Healthcare cybersecurity workforce\n##### (a) Training for healthcare experts\nThe Secretary, in coordination with the Cybersecurity State Coordinators of the Agency and private sector health care experts, as appropriate, shall provide training to Healthcare and Public Health Sector asset owners and operators on\u2014\n**(1)**\ncybersecurity risks to information systems within the Healthcare and Public Health Sector; and\n**(2)**\nways to mitigate the risks to information systems in the Healthcare and Public Health Sector.\n##### (b) Cross-Agency educational tools\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary, acting through the Administrator of the Health Resources and Services Administration, in coordination with the Agency, shall develop a strategic plan to support growing the cybersecurity workforce for health care entities.\n**(2) Inclusions**\nThe strategic plan under paragraph (1) shall include\u2014\n**(A)**\nrecommendations for existing educational programs that can be used to support cybersecurity training;\n**(B)**\ndissemination and development of educational materials on how to improve cybersecurity resilience;\n**(C)**\ndevelopment of best practices to train the health care workforce on cybersecurity best practices; and\n**(D)**\nopportunities for public-private collaboration to strengthen the cybersecurity workforce.",
      "versionDate": "2026-03-23",
      "versionType": "Reported in Senate"
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-03-26T18:53:41Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-03-26T18:53:12Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-03-26T18:53:36Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-03-26T18:53:31Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2026-03-26T18:53:19Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-03-26T18:54:01Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-03-26T18:53:27Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-03-26T18:53:50Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2026-03-26T18:53:54Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-03-26T18:54:06Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2026-03-26T18:53:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-03-27T14:49:39Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3315is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-03-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3315rs.xml"
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
      "title": "Health Care Cybersecurity and Resiliency Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T05:23:21Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Health Care Cybersecurity and Resiliency Act of 2026",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-03-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Health Care Cybersecurity and Resiliency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-20T06:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Health and Human Services and the Director of the Cybersecurity and Infrastructure Security Agency to coordinate to improve cybersecurity in the health care and public health sectors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T06:18:34Z"
    }
  ]
}
```
