# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2947?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2947
- Title: Pray Safe Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2947
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2026-03-03T12:03:26Z
- Update date including text: 2026-03-03T12:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in Senate
- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-09-30: Introduced in Senate

## Actions

- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2947",
    "number": "2947",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Pray Safe Act of 2025",
    "type": "S",
    "updateDate": "2026-03-03T12:03:26Z",
    "updateDateIncludingText": "2026-03-03T12:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-30",
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
            "date": "2025-09-30T18:54:49Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-30T18:54:49Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "WI"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MI"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "OK"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "AZ"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NV"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MI"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "TX"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "OH"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "GA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-28",
      "state": "ME"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2947is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2947\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Ms. Hassan (for herself, Mr. Johnson , Mr. Peters , Mr. Lankford , Mr. Kelly , Mr. Scott of Florida , Ms. Rosen , and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo establish a Federal Clearinghouse on Safety and Best Practices for Nonprofit Organizations, Faith-based Organizations, and Houses of Worship within the Department of Homeland Security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pray Safe Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Clearinghouse**\nThe term Clearinghouse means the Federal Clearinghouse on Safety and Security Best Practices for Nonprofit Organizations, Faith-based Organizations, and Houses of Worship established under section 3(a).\n**(2) Department**\nThe term Department means the Department of Homeland Security.\n**(3) Faith-based organization**\nThe term faith-based organization means a group, center, or nongovernmental organization with a religious, ideological, or spiritual motivation, character, affiliation, or purpose that meets the definition of nonprofit organization.\n**(4) House of worship**\nThe term house of worship means a place or building, including a synagogue, mosque, temple, and church, in which congregants practice their religious or spiritual beliefs.\n**(5) Nonprofit organization**\nThe term nonprofit organization means an organization\u2014\n**(A)**\nof the type described in subsection (c)(3) of section 501 of the Internal Revenue Code of 1986 and exempt from taxation under subsection (a) of such section; and\n**(B)**\ndetermined to be at risk of a terrorist attack or other threat by the Secretary.\n**(6) Safety and security**\nThe term safety and security means prevention of, protection against, or recovery from threats and incidents, including natural disasters, manmade disasters, or terrorist attacks.\n**(7) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n#### 3. Federal Clearinghouse on Safety and Security Best Practices for Nonprofit Organizations, Faith-based Organizations, and Houses of Worship\n##### (a) Federal Clearinghouse\n**(1) Establishment**\n**(A) In general**\nNot later than 270 days after the date of enactment of this Act, the Secretary, in consultation with the Attorney General, the Executive Director of the White House Office of Faith-Based and Neighborhood Partnerships, and the head of any other agency the Secretary determines appropriate, shall establish within the Department a Federal Clearinghouse on Safety and Security Best Practices for Nonprofit Organizations, Faith-based Organizations, and Houses of Worship.\n**(B) Purpose**\nThe Clearinghouse shall be the primary resource of the Federal Government to\u2014\n**(i)**\neducate and publish online best practices and recommendations for safety and security for nonprofit organizations, including faith-based organizations, and houses of worship; and\n**(ii)**\nprovide information relating to Federal grant programs available to nonprofit organizations, including faith-based organizations, and houses of worship.\n**(C) Personnel**\n**(i) Assignments**\nThe Clearinghouse shall be assigned such personnel and resources as the Secretary considers appropriate to carry out this subsection.\n**(ii) Detailees**\nThe Secretary may coordinate detailees on a reimbursable or a nonreimbursable basis as required for the Clearinghouse.\n**(iii) Designated point of contact**\n**(I) In general**\nThere shall be not fewer than 1 employee assigned or detailed to the Clearinghouse who shall be the designated point of contact to provide information and assistance to nonprofit organizations, including faith-based organizations, and houses of worship, including assistance relating to the grant program established under subsection (c).\n**(II) Contact information**\nThe contact information of the designated point of contact under subclause (I) shall be made available on the website of the Clearinghouse.\n**(iv) Qualification**\nTo the maximum extent possible, any personnel assigned or detailed to the Clearinghouse under this subparagraph should be familiar with nonprofit organizations, including faith-based organizations, and houses of worship and with physical and online security measures to identify and prevent safety and security risks.\n**(2) Clearinghouse contents**\n**(A) Evidence-based tiers**\n**(i) In general**\nThe Secretary, in consultation with the Attorney General, the Executive Director of the White House Office of Faith-Based and Neighborhood Partnerships, and the head of any other agency the Secretary determines appropriate, shall develop tiers for determining evidence-based best practices and recommendations that demonstrate a significant effect on improving safety and security of nonprofit organizations, including faith-based organizations, and houses of worship.\n**(ii) Requirements**\nThe tiers required to be developed under clause (i) shall\u2014\n**(I)**\nprioritize\u2014\n**(aa)**\nstrong evidence from not fewer than 1 well-designed and well-implemented experimental study; and\n**(bb)**\nmoderate evidence from not fewer than 1 well-designed and well-implemented quasi-experimental study; and\n**(II)**\nconsider promising evidence that demonstrates a rationale based on high-quality research findings or positive evaluations that the activity, strategy, or intervention is likely to improve and promote safety and security of nonprofit organizations, including faith-based organizations, and houses of worship.\n**(B) Criteria for best practices and recommendations**\nThe best practices and recommendations referred to in paragraph (1)(B)(i) of the Clearinghouse shall, at a minimum\u2014\n**(i)**\nidentify areas of concern for nonprofit organizations, including faith-based organizations, and houses of worship, including event planning recommendations, checklists, facility hardening, tabletop exercise resources, and other resilience measures;\n**(ii)**\ninvolve comprehensive safety and security measures, including threat prevention, preparedness, protection, mitigation, incident response, and recovery to improve the safety and security posture of nonprofit organizations, including faith-based organizations, and houses of worship upon implementation;\n**(iii)**\ninvolve comprehensive safety and security measures, including preparedness, protection, mitigation, incident response, and recovery to improve the resiliency of nonprofit organizations, including faith-based organizations, and houses of worship from threats and incidents, including natural disasters, manmade disasters, or terrorist attacks or other threats;\n**(iv)**\ninclude any evidence or research rationale supporting the determination of the Clearinghouse that the comprehensive safety and security measures under clauses (ii) and (iii) have been shown to have a significant effect on improving the safety and security of individuals who, at the time of any such threat or incident, are physically located in the place or building of a nonprofit organization, including a faith-based organization, or a house of worship, including\u2014\n**(I)**\nfindings and data from previous Federal, State, local, Tribal, territorial, private sector, and nongovernmental organization research centers relating to the safety and security of nonprofit organizations, including faith-based organizations, and houses of worship, including from targeted violence; and\n**(II)**\nother supportive evidence or findings relied upon by the Clearinghouse in determining best practices and recommendations to improve the safety and security posture of nonprofit organizations, including faith-based organizations, and houses of worship upon implementation; and\n**(v)**\ninclude an overview of the available resources the Clearinghouse can provide to nonprofit organizations and houses of worship.\n**(C) Additional information**\nThe Clearinghouse shall maintain and make available a comprehensive index of all Federal grant programs for which nonprofit organizations, including faith-based organizations, and houses of worship are eligible, which shall include the performance metrics the recipient will be required to provide for each grant.\n**(D) Past recommendations**\nTo the greatest extent practicable, the Clearinghouse shall identify and present, as appropriate, best practices and recommendations issued by Federal, State, local, Tribal, territorial, private sector, and nongovernmental organizations relevant to the safety and security of nonprofit organizations, including faith-based organizations, and houses of worship.\n**(E) Existing platform**\nThe Secretary may establish and maintain the Clearinghouse on an online platform or a website that is in existence as of the date of enactment of this Act.\n**(3) Assistance and training**\nThe Secretary may produce and publish materials on the Clearinghouse to assist and train nonprofit organizations, including faith-based organizations, and houses of worship regarding the implementation of the best practices and recommendations under this subsection.\n**(4) Continuous improvement**\n**(A) In general**\nThe Secretary shall\u2014\n**(i)**\ncollect for the purpose of continuous improvement of the Clearinghouse\u2014\n**(I)**\nClearinghouse data analytics;\n**(II)**\nuser feedback on the implementation of resources, best practices, and recommendations identified by the Clearinghouse; and\n**(III)**\nany evaluations conducted regarding implementation of such best practices and recommendations;\n**(ii)**\nin coordination with the Faith-Based Security Advisory Council of the Department, the Department of Justice, the Executive Director of the White House Office of Faith-Based and Neighborhood Partnerships, and any other agency the Secretary determines appropriate\u2014\n**(I)**\nassess and identify Clearinghouse best practices and recommendations for which there are no resources available through Federal Government programs for implementation;\n**(II)**\nprovide feedback on the implementation of such best practices and recommendations; and\n**(III)**\npropose additional best practices and recommendations for inclusion in the Clearinghouse; and\n**(iii)**\nnot less frequently than annually, examine and update the Clearinghouse in accordance with\u2014\n**(I)**\nthe information collected under clause (i); and\n**(II)**\nthe best practices and recommendations proposed under clause (ii)(III).\n**(B) Report to Congress**\nNot later than 3 years after the date of enactment of this Act, and every 3 years thereafter during the period in which the Clearinghouse is in existence, the Secretary shall submit to Congress a report on the updates under subparagraph (A)(iii) made to the Clearinghouse during the preceding 3-year period, which shall include a description of any changes made pursuant thereto to the Clearinghouse.\n##### (b) Notification of the Clearinghouse\n**(1) In general**\nThe Secretary shall provide to the individuals, Federal agencies, and committees specified in paragraph (2) written notification of the establishment of the Clearinghouse, including updates pertaining to grant programs identified under subsection (a)(2)(C).\n**(2) Individuals, Federal agencies, and committees specified**\nThe individuals, Federal entities, and committees specified in this paragraph are the following:\n**(A)**\nEvery State homeland security advisor.\n**(B)**\nEvery State department of homeland security.\n**(C)**\nOther Federal agencies with grant programs or initiatives that aid in the safety and security of nonprofit organizations, including faith-based organizations, and houses of worship, as determined appropriate by the Secretary.\n**(D)**\nEvery Cyber Security Advisor.\n**(E)**\nEvery Protective Security Advisor.\n**(F)**\nEvery Federal Bureau of Investigation Joint Terrorism Task Force.\n**(G)**\nEvery Homeland Security Fusion Center.\n**(H)**\nEvery State or territorial Governor or other chief executive.\n**(I)**\nThe Committee on Homeland Security and Governmental Affairs and the Committee on the Judiciary of the Senate.\n**(J)**\nThe Committee on Homeland Security and the Committee on the Judiciary of the House of Representatives.\n##### (c) Federal grants and resources overview\n**(1) In general**\nTo the extent practicable, the Secretary, when carrying out subsection (a)(2)(C), shall include a grants program overview on the website of the Clearinghouse that shall\u2014\n**(A)**\nbe a location for all information regarding Federal grant programs that are open to nonprofit organizations, including faith-based organizations, and houses of worship for the purposes of safety and security;\n**(B)**\ndirectly link to each grant application and any applicable user guides;\n**(C)**\nidentify all safety and security homeland security assistance programs managed by the Department that may be used to implement best practices and recommendations of the Clearinghouse;\n**(D)**\nconcurrent with the application period for any grant identified under subsection (a)(2)(C), provide information related to the required elements of grant applications to aid nonprofit organizations, including faith-based organizations, and houses of worship in meeting the eligibility criteria for Federal grants; and\n**(E)**\nprovide answers to frequently asked questions regarding the implementation of best practices and recommendations of the Clearinghouse and best practices for applying for a grant identified under subsection (a)(2)(C).\n**(2) Provision of information relating to Federal grants and resources**\nEach Federal agency notified under subsection (b) shall provide to the Secretary or other appropriate point of contact for the Clearinghouse for inclusion in the Clearinghouse necessary information regarding any Federal grant programs or resources of the Federal agency that are available for nonprofit organizations, including faith-based organizations, and houses of worship.\n**(3) State grants and resources**\n**(A) In general**\nAny State notified under subsection (b) may provide to the Secretary or other appropriate point of contact for the Clearinghouse for inclusion in the Clearinghouse necessary information regarding any grant programs or resources of the State available for nonprofit organizations, including faith-based organizations, and houses of worship for the purposes of safety and security.\n**(B) Identification of resources**\nThe Clearinghouse shall, to the extent practicable, identify for each State the following:\n**(i)**\nEach State agency responsible for safety and security of nonprofit organizations, including faith-based organizations, and houses of worship in the State, or any State that does not have such an agency designated.\n**(ii)**\nAny grant program that may be used for the purposes of implementing best practices and recommendations of the Clearinghouse.\n**(iii)**\nAny resources or programs, including community prevention or intervention efforts, that may be used to assist in targeted violence and terrorism prevention.\n##### (d) Other resources\nThe Secretary shall, on the website of the Clearinghouse, include a separate section for other resources that shall provide a centralized list of all available points of contact from which a nonprofit organization, including a faith-based organization, or a house of worship may seek assistance in grant applications and in carrying out the best practices and recommendations of the Clearinghouse, including the following:\n**(1)**\nA list of contact information to reach Department personnel to assist with grant-related questions.\n**(2)**\nThe applicable Agency contact information to connect houses of worship with Protective Security Advisors.\n**(3)**\nContact information for all Department Fusion Centers, listed by State.\n**(4)**\nInformation on the If you See Something Say Something Campaign of the Department.\n**(5)**\nAny other appropriate contacts.\n##### (e) Rule of construction\nNothing in this section may be construed to create, satisfy, or waive any requirement under Federal civil rights laws, including\u2014\n**(1)**\ntitle II of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12131 et seq. ); or\n**(2)**\ntitle VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ).\n##### (f) Sunset\nThis Act shall cease to be effective on the date that is 4 years after the date of enactment of this Act.\n#### 4. GAO report\nThe Comptroller General of the United States shall submit to Congress a report on the state of Federal grants devoted to safety and security for nonprofit organizations, including faith-based organizations, and houses of worship, and an evaluation of the relevant programs and resources devoted to the safety and security of nonprofit organizations, including faith-based organizations, and houses of worship as of the date of the report.",
      "versionDate": "2025-09-30",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-09-30",
        "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5645",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Pray Safe Act of 2025",
      "type": "HR"
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
        "name": "Emergency Management",
        "updateDate": "2025-12-05T21:47:51Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2947is.xml"
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
      "title": "Pray Safe Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T12:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pray Safe Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-11T02:53:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a Federal Clearinghouse on Safety and Best Practices for Nonprofit Organizations, Faith-based Organizations, and Houses of Worship within the Department of Homeland Security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-11T02:48:14Z"
    }
  ]
}
```
