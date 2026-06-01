# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4502?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4502
- Title: Silver Shield Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4502
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2026-04-03T08:05:51Z
- Update date including text: 2026-04-03T08:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4502",
    "number": "4502",
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
    "title": "Silver Shield Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-03T08:05:51Z",
    "updateDateIncludingText": "2026-04-03T08:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
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
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:08:50Z",
          "name": "Referred To"
        }
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
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "PA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "MA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "WA"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "WI"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4502ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4502\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Ms. Jacobs (for herself, Ms. Dean of Pennsylvania , Mr. Keating , and Mr. Castro of Texas ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo impose requirements with respect to monitoring the operational use of sales, exports, and transfers of defense articles and services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Silver Shield Operational End Use Monitoring Act of 2025 or the Silver Shield Act of 2025 .\n#### 2. Establishment of silver shield operational end-use monitoring program\n##### (a) Establishment of operational end-Use monitoring program\n**(1) In general**\nIn order to improve accountability with respect to defense articles and defense services sold, leased, transferred, or exported under the Arms Export Control Act ( 22 U.S.C. 2751 et seq. ) or the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ), not later than 1 year after the date of the enactment of this Act, the President shall establish a program, to be known as the Silver Shield program, to provide for operational end-use monitoring of such articles and services.\n**(2) Requirements of program**\nThe Silver Shield program shall\u2014\n**(A)**\nbe designed to monitor whether there is credible information that a recipient used defense articles or defense services from the United States to inflict civilian harm, violate international humanitarian law, or violate international human rights law;\n**(B)**\ndetermine through operational end-use monitoring whether defense articles or defense services from the United States were used to commit\u2014\n**(i)**\ngenocide;\n**(ii)**\ncrimes against humanity;\n**(iii)**\ngrave breaches of the Geneva Conventions of 1949; or\n**(iv)**\nother serious violations of international humanitarian or human rights law;\n**(C)**\nrequire a determination of ineligibility, pursuant to section 3 of the Arms Export Control Act, should a determination described in subparagraph (B) be affirmative, including a timeline of 180 days to complete such determinations on such allegations of violation;\n**(D)**\nincorporate data, best practices, and lessons learned from the implementation of\u2014\n**(i)**\nthe Civilian Harm Incident Response Guidance;\n**(ii)**\nprograms to carry out the requirements of section 362 of title 10, United States Code and section 620M of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2378d ) (collectively referred to as the Leahy Laws );\n**(iii)**\nNational Security Memorandum 20;\n**(iv)**\nthe Golden Sentry End-Use Monitoring Program; and\n**(v)**\nthe Blue Lantern program; and\n**(E)**\nincorporates sources of information for monitoring including\u2014\n**(i)**\nreports submitted by United States Government personnel, including United States embassy, Defense Security Cooperation Agency, or combatant command personnel;\n**(ii)**\neyewitness interviews;\n**(iii)**\npublicly available photographic and video evidence;\n**(iv)**\nsatellite imagery;\n**(v)**\ncredible reports by non-governmental organizations and media;\n**(vi)**\nintelligence information;\n**(vii)**\ninformation submitted through a publicly available online portal to be integrated with the Human Rights Reporting Gateway;\n**(viii)**\nrelevant forensic investigations;\n**(ix)**\nsite visits by United States Government personnel; and\n**(x)**\nany other credible sources of information regarding the use of United States origin defense articles or defense services in inflicting civilian harm or to commit a violation of international humanitarian law or international human rights law.\n**(3) Coordination**\nThe Silver Shield program shall be established in the Department of State and shall be implemented through coordination between the following:\n**(A)**\nThe Bureau of Democracy, Human Rights, and Labor, which shall in coordination with the Bureau of Political-Military Affairs of the Department of State be responsible for directing and managing the implementation of the program.\n**(B)**\nThe Office of the Secretary, the Defense Security Cooperation Agency, and the Civilian Protection Center of Excellence of the Department of Defense.\n**(C)**\nAny other Federal department or agency the President determines relevant to the establishment or implementation of the Silver Shield program.\n**(4) Consultation**\nThe Silver Shield program shall take such steps as may be necessary to consult as appropriate with relevant experts affiliated with federally funded research and development corporations, non-governmental organizations, and academic institutions.\n##### (b) External advisory board\nThe President shall establish an external advisory board comprising recognized academic and non-governmental experts in investigations regarding the monitoring of the usage of defense articles or services in civilian harm or violations of international law. The heads of the agencies listed in subsection (a)(3) shall periodically consult with the external advisory board with respect to\u2014\n**(1)**\nresearch methodology;\n**(2)**\ninformation sources;\n**(3)**\ninvestigative best practices; and\n**(4)**\nany other such information within the expertise of the advisory board and relevant to implementation of this Act.\n#### 3. Amendments to the Arms Export Control Act\n##### (a) Arms export control act\nSection 3 of the Arms Export Control Act ( 22 U.S.C. 2753 ) is amended by adding at the end of the section the following\u2014\n(h) Agreement relating to use of defense articles and services In addition to any other requirements under this Act, the President shall take such steps as may be necessary to ensure that\u2014 (1) prior to authorizing or licensing the sale, export, or transfer of any defense article or defense service to a foreign country or international organization, the Secretary of State shall enter into a written agreement with the appropriate counterparts providing that the government of such country or that such international organization will not use any defense article or defense service of United States origin\u2014 (A) to commit or facilitate a violation of international humanitarian law or international human rights law; or (B) in an action that would render the government or organization ineligible to receive United States assistance or arms transfers as a matter of United States law; and (2) if defense articles are sold, exported, or transferred to a foreign country pursuant to an agreement otherwise in accordance with the requirements of this Act in which the intended end-user has not been identified at the unit level for purposes of the vetting required by section 362 of title 10, United States Code or section 620M of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2378d ), the written agreement required by paragraph (1) for such sale, export, or transfer shall instead include a list of units ineligible to receive such articles, consistent with applicable provisions of United States law. .\n##### (b) Eligibility for defense articles or services\n**(1) Arms Export Control Act**\nSection 3(a) of the Arms Export Control Act ( 22 U.S.C. 2753(a) ) is amended\u2014\n**(A)**\nin paragraph (1), by striking and promote world peace and inserting , will promote world peace and the safety of civilians, ;\n**(B)**\nin paragraph (3), by striking ; and and inserting a semicolon;\n**(C)**\nby redesignating paragraph (4) as paragraph (5); and\n**(D)**\nby inserting after paragraph (3) the following new paragraph:\n(4) the country or international organization shall have agreed not to use such article or service to commit or facilitate a serious violation of international humanitarian law or international human rights law; and .\n**(2) Foreign Assistance Act of 1961**\nSection 505 of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2314 ) is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nby striking (a) Conditions of eligibility and all that follows through the matter preceding paragraph (1) and inserting the following:\n(a) Conditions of eligibility In addition to such other provisions as the President may require, no defense articles or related training or other defense service shall be furnished to any country or international organization on a grant basis unless it shall have agreed that\u2014 ;\n**(ii)**\nin paragraph (3), by striking ; and and inserting a semicolon;\n**(iii)**\nby redesignating paragraph (4) as paragraph (5); and\n**(iv)**\nby inserting after paragraph (3) the following new paragraph:\n(4) it will not use such articles or services to commit or facilitate a serious violation of international humanitarian law or international human rights law; and ; and\n**(B)**\nin subsection (e), by striking subsection (a)(1) or (a)(4) each place it appears and inserting subsection (a)(1) or (a)(5) .\n##### (c) Authorized purpose for military sales\nSection 4 of the Arms Export Control Act ( 22 U.S.C. 2754 ) is amended\u2014\n**(1)**\nby inserting legitimate before internal security ; and\n**(2)**\nby inserting , to the extent that such defense articles and defense services will not be used in the commission of a serious violation of international humanitarian law or international human rights law. The violation of international humanitarian law or international human rights law may not be construed to be an authorized purpose for military sales or leases by the United States. after such friendly countries .\n##### (d) Effective date\nThe amendments made by this section shall take effect 1 year after the date of the enactment of this Act.\n##### (e) Updates to existing policy\n**(1) Secretary of State**\nThe Secretary of State shall\u2014\n**(A)**\nsubsume the Civilian Harm Incident Response Guidance into the requirements of this Act to carry out the Department\u2019s operational end-use monitoring responsibilities; and\n**(B)**\nreview other relevant policy and doctrine and, as necessary, amend any such policy or doctrine to ensure consistency with such amendments and to carry out such responsibilities.\n**(2) Secretary of Defense**\nThe Secretary of Defense shall\u2014\n**(A)**\nreissue Department of Defense Instruction 4140.66 to ensure consistency with the amendments made by this Act to carry out the Department\u2019s operational end-use monitoring responsibilities; and\n**(B)**\nreview other relevant policy and doctrine and, as necessary, amend any such policy or doctrine to ensure consistency with such amendments and to carry out such responsibilities.\n#### 4. Authorization of appropriations\n##### (a) Authorization\nThere is authorized to be appropriated such sums as may be necessary to implement the Silver Shield program described in section 2.\n##### (b) Application of foreign military sales administrative surcharge\nThe Silver Shield program shall be considered an administrative service of the administration of sales made pursuant to section 21(e)(1) of the Arms Export Control Act ( 22 U.S.C. 2761 ).\n##### (c) Application of foreign military financing administrative funds\nThe Silver Shield program shall be considered an administrative and operational cost of the Department of State related to military assistance and sales pursuant to funds authorized to carry out title IV of the annual Acts making appropriations for the State Department, Foreign Operations, and Related programs (relating to the heading Foreign Military Financing program).\n#### 5. Reports\n##### (a) Report on required resources\nNot later than 180 days after the enactment of this Act, the Secretary of State shall submit to the appropriate congressional committees a report on the necessary resources, staffing, and authorities to implement the Silver Shield program and requirements described in section 2(a).\n##### (b) Annual implementation report\nNot later than 1 year after the establishment of the program required by section 2, and annually thereafter as a part of the annual congressional presentation documents submitted under section 634 of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2394 ), the President shall submit to the appropriate congressional committees a report describing the actions taken to implement this Act and the amendments made by this Act, including the following:\n**(1)**\nA detailed accounting of the costs and number of personnel associated with the Silver Shield program.\n**(2)**\nResource constraints associated with the implementation of the program, including staffing, funding, and authorities.\n**(3)**\nThe numbers and range of operational end-use monitoring of United States arms transfers.\n**(4)**\nThe number of identified incidents for which investigations have not yet been initiated.\n**(5)**\nThe number and status of ongoing investigations, including the stage they are in, how long such incidents have remained in such stage, and if any have remained in such stage for more than 1 year.\n#### 6. Definitions\nIn this Act:\n##### (a) Appropriate congressional committees\nThe term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Affairs, the Committee on Armed Services, and the Committee on Appropriations of the House of Representatives; and\n**(2)**\nthe Committee on Foreign Relations, the Committee on Armed Services, and the Committee on Appropriations of the Senate.\n##### (b) Civilian harm\nThe term civilian harm means civilian casualties, damage to or destruction of civilian objects, and significant adverse effects on the civilian population and the personnel, organizations, resources, infrastructure, essential services, and systems on which civilian life depends resulting from military operations.\n##### (c) Defense article; Defense service\nThe terms defense article and defense service have the meanings given those terms in section 47 of the Arms Export Control Act ( 22 U.S.C. 2794 ).\n##### (d) Operational end-Use monitoring\nThe term operational end-use monitoring means gathering and assessing information regarding the use of a defense article or defense service, including in civilian harm, violations of international humanitarian law, or international human rights law.",
      "versionDate": "2025-07-17",
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
        "name": "International Affairs",
        "updateDate": "2025-08-01T17:24:24Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4502ih.xml"
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
      "title": "Silver Shield Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Silver Shield Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Silver Shield Operational End Use Monitoring Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To impose requirements with respect to monitoring the operational use of sales, exports, and transfers of defense articles and services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:33:26Z"
    }
  ]
}
```
