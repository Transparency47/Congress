# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3841?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3841
- Title: Healthcare Cybersecurity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3841
- Origin chamber: House
- Introduced date: 2025-06-09
- Update date: 2026-05-16T08:07:51Z
- Update date including text: 2026-05-16T08:07:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-09: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-09 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-10 - Committee: Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.
- Latest action: 2025-06-09: Introduced in House

## Actions

- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-09 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-10 - Committee: Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3841",
    "number": "3841",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Healthcare Cybersecurity Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:51Z",
    "updateDateIncludingText": "2026-05-16T08:07:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Cybersecurity and Infrastructure Protection Subcommittee",
          "systemCode": "hshm08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-09",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-09",
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
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-09",
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
          "date": "2025-06-09T16:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-10T20:28:46Z",
              "name": "Referred to"
            }
          },
          "name": "Cybersecurity and Infrastructure Protection Subcommittee",
          "systemCode": "hshm08"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-09T16:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "PA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3841ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3841\nIN THE HOUSE OF REPRESENTATIVES\nJune 9, 2025 Mr. Crow (for himself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Homeland Security , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo enhance the cybersecurity of the Healthcare and Public Health Sector.\n#### 1. Short title\nThis Act may be cited as the Healthcare Cybersecurity Act of 2025 .\n#### 2. Definitions\nIn this Act\u2014\n**(1)**\nthe term Agency means the Cybersecurity and Infrastructure Security Agency;\n**(2)**\nthe term covered asset means a Healthcare and Public Health Sector asset, including technologies, services, and utilities;\n**(3)**\nthe term Cybersecurity State Coordinator means a Cybersecurity State Coordinator appointed under section 2217(a) of the Homeland Security Act of 2002 ( 6 U.S.C. 665c(a) );\n**(4)**\nthe term Department means the Department of Health and Human Services;\n**(5)**\nthe term Director means the Director of the Agency;\n**(6)**\nthe term Healthcare and Public Health Sector means the Healthcare and Public Health sector, as identified in the National Security Memorandum on Critical Infrastructure and Resilience (NSM\u201322), issued April 30, 2024;\n**(7)**\nthe term Information Sharing and Analysis Organizations has the meaning given the term in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 );\n**(8)**\nthe term Plan means the Healthcare and Public Health Sector-specific Risk Management Plan; and\n**(9)**\nthe term Secretary means the Secretary of Health and Human Services.\n#### 3. Findings\nCongress finds the following:\n**(1)**\nCovered assets are increasingly the targets of malicious cyberattacks, which result not only in data breaches but also increased healthcare delivery costs and can ultimately affect patient health outcomes.\n**(2)**\nData reported to the Department shows that large cyber breaches of the information systems of healthcare facilities rose 93 percent between 2018 and 2022.\n**(3)**\nAccording to the Annual Report to Congress on Breaches of Unsecured Protected Health Information for Calendar Year 2022 issued by the Office for Civil Rights of the Department, breaches of unsecured protected health information have increased 107 percent since 2018, and, in 2022 alone, the Department received 626 reported breaches affecting not fewer than 500 individuals at covered entities or business associates (as defined in section 160.103 of title 45, Code of Federal Regulations) that occurred or ended in 2022, with nearly 42,000,000 individuals affected.\n#### 4. Agency coordination with the Department\n##### (a) In general\nThe Agency shall coordinate with the Department to improve cybersecurity in the Healthcare and Public Health Sector.\n##### (b) Agency liaison to the Department\n**(1) Appointment**\nThe Director shall, in coordination with the Secretary, appoint an individual, who shall be an employee of the Agency or a detailee assigned to the Administration for Strategic Preparedness and Response Office of the Department by the Director, to serve as a liaison of the Agency to the Department, who shall\u2014\n**(A)**\nhave appropriate cybersecurity qualifications and expertise; and\n**(B)**\nreport directly to the Director.\n**(2) Responsibilities and duties**\nThe liaison appointed under paragraph (1) shall\u2014\n**(A)**\nserve as a primary contact of the Department to coordinate cybersecurity issues with the Agency;\n**(B)**\nsupport the implementation and execution of the Plan and assist in the development of updates to the Plan;\n**(C)**\nfacilitate the sharing of cyber threat information between the Department and the Agency to improve understanding of cybersecurity risks and situational awareness of cybersecurity incidents;\n**(D)**\nassist in implementing the training described in section 5;\n**(E)**\nfacilitate coordination between the Agency and the Department during cybersecurity incidents within the Healthcare and Public Health Sector; and\n**(F)**\nperform such other duties as determined necessary by the Secretary to achieve the goal of improving the cybersecurity of the Healthcare and Public Health Sector.\n**(3) Report**\n**(A) Requirement**\nNot later than 18 months after the date of enactment of this Act, the Secretary, in coordination with the Director, shall submit a report that describes the activities undertaken to improve cybersecurity coordination between the Agency and the Department to\u2014\n**(i)**\nthe Committee on Health, Education, Labor, and Pensions, the Committee on Finance, and the Committee on Homeland Security and Governmental Affairs of the Senate; and\n**(ii)**\nthe Committee on Energy and Commerce, the Committee on Ways and Means, and the Committee on Homeland Security of the House of Representatives.\n**(B) Contents**\nThe report submitted under subparagraph (A) shall include\u2014\n**(i)**\na summary of the activities of the liaison appointed under paragraph (1);\n**(ii)**\na description of any challenges to the effectiveness of the liaison appointed under paragraph (1) completing the required duties of the liaison; and\n**(iii)**\na study of the feasibility of an agreement to improve cybersecurity in the public sector of healthcare.\n##### (c) Resources\n**(1) In general**\nThe Agency shall coordinate with and make resources available to Information Sharing and Analysis Organizations, information sharing and analysis centers, the sector coordinating councils, and non-Federal entities that are receiving information shared through programs managed by the Department.\n**(2) Scope**\nThe coordination under paragraph (1) shall include\u2014\n**(A)**\ndeveloping products specific to the needs of Healthcare and Public Health Sector entities; and\n**(B)**\nsharing information relating to cyber threat indicators and appropriate defensive measures.\n#### 5. Training for healthcare owners and operators\nThe Agency shall make available training to the owners and operators of covered assets on\u2014\n**(1)**\ncybersecurity risks to the Healthcare and Public Health Sector and covered assets; and\n**(2)**\nways to mitigate the risks to information systems in the Healthcare and Public Health Sector.\n#### 6. Sector-specific risk management plan\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary, in coordination with the Director, shall update the Plan, which shall include the following elements:\n**(1)**\nAn analysis of how identified cybersecurity risks specifically impact covered assets, including the impact on rural and small- and medium-sized covered assets.\n**(2)**\nAn evaluation of the challenges the owners and operators of covered assets face in\u2014\n**(A)**\nsecuring\u2014\n**(i)**\nupdated information systems owned, leased, or relied upon by covered assets;\n**(ii)**\nmedical devices or equipment owned, leased, or relied upon by covered assets, which shall include an analysis of the threat landscape and cybersecurity vulnerabilities of such medical devices or equipment; and\n**(iii)**\nsensitive patient health information and electronic health records;\n**(B)**\nimplementing cybersecurity protocols; and\n**(C)**\nresponding to data breaches or cybersecurity attacks, including the impact on patient access to care, quality of patient care, timeliness of health care delivery, and health outcomes.\n**(3)**\nAn evaluation of the best practices for utilization of resources from the Agency to support covered assets before, during, and after data breaches or cybersecurity attacks, such as by Cyber Security Advisors and Cybersecurity State Coordinators of the Agency or other similar resources.\n**(4)**\nAn assessment of relevant Healthcare and Public Health Sector cybersecurity workforce shortages, including\u2014\n**(A)**\ntraining, recruitment, and retention issues; and\n**(B)**\nrecommendations for how to address these shortages and issues, particularly at rural and small- and medium-sized covered assets.\n**(5)**\nAn evaluation of the most accessible and timely ways for the Agency and the Department to communicate and deploy cybersecurity recommendations and tools to the owners and operators of covered assets.\n##### (b) Congressional briefing\nNot later than 120 days after the date of enactment of this Act, the Secretary, in consultation with the Director, shall provide a briefing on the updating of the Plan under subsection (a) to\u2014\n**(1)**\nthe Committee on Health, Education, Labor, and Pensions, the Committee on Finance, and the Committee on Homeland Security and Governmental Affairs of the Senate; and\n**(2)**\nthe Committee on Energy and Commerce, the Committee on Ways and Means, and the Committee on Homeland Security of the House of Representatives.\n#### 7. Identifying high-risk covered assets\n##### (a) In general\nThe Secretary, in consultation with the Director and health sector owners and operators, as appropriate, may establish objective criteria for determining whether a covered asset may be designated as a high-risk covered asset, provided that such criteria shall align with the methodology promulgated by the Director for identifying functions relating to critical infrastructure, as defined in section 1016(e) of the Critical Infrastructures Protection Act of 2001 ( 42 U.S.C. 5195c(e) ), and associated risk assessments.\n##### (b) List of high-Risk covered assets\n**(1) In general**\nThe Secretary may develop a list of, and notify, the owners and operators of each covered asset determined to be a high-risk covered asset using the methodology promulgated by the Director pursuant to subsection (a).\n**(2) Biannual updating**\nThe Secretary may\u2014\n**(A)**\nbiannually review and update the list of high-risk covered assets developed under paragraph (1); and\n**(B)**\nnotify the owners and operators of each covered asset added to or removed from the list as part of a review and update of the list under subparagraph (A).\n**(3) Notice to Congress**\nThe Secretary shall notify Congress when an initial list of high-risk covered assets is developed under paragraph (1) and each time the list is updated under paragraph (2).\n**(4) Use**\nThe list developed and updated under this subsection may be used by the Department to prioritize resource allocation to high-risk covered assets to bolster cyber resilience.\n#### 8. Reports\n##### (a) Report on assistance provided to entities of Healthcare and Public Health Sector\nNot later than 120 days after the date of enactment of this Act, the Agency shall submit to Congress a report on the organization-wide level of support and activities that the Agency has provided to the healthcare and public health sector to proactively prepare the sector to face cyber threats and respond to cyber attacks when such threats or attacks occur.\n##### (b) Report on critical infrastructure resources\nNot later than 18 months after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress a report on Federal resources available, as of the date of enactment of this Act, for the Healthcare and Public Health Sector relating to critical infrastructure, as defined in section 1016(e) of the Critical Infrastructures Protection Act of 2001 ( 42 U.S.C. 5195c(e) ), including resources available from recent and ongoing collaboration with the Director and the Secretary.\n#### 9. Rules of construction\n##### (a) Agency actions\nNothing in this Act shall be construed to authorize the Secretary or Director to take an action that is not authorized by this Act or existing law.\n##### (b) Protection of rights\nNothing in this Act shall be construed to permit the violation of the rights of any individual protected by the Constitution of the United States, including through censorship of speech protected by the Constitution of the United States or unauthorized surveillance.\n##### (c) No additional funds\nNo additional funds are authorized to be appropriated for the purpose of carrying out this Act.",
      "versionDate": "2025-06-09",
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
        "actionDate": "2025-05-21",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "1851",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Healthcare Cybersecurity Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-06-27T13:01:46Z"
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
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3841ih.xml"
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
      "title": "Healthcare Cybersecurity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthcare Cybersecurity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance the cybersecurity of the Healthcare and Public Health Sector.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:33:18Z"
    }
  ]
}
```
