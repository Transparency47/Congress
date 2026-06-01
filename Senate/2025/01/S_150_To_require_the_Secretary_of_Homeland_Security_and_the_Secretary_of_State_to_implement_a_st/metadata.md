# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/150?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/150
- Title: Combating Cartels on Social Media Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 150
- Origin chamber: Senate
- Introduced date: 2025-01-17
- Update date: 2025-12-05T21:58:13Z
- Update date including text: 2025-12-05T21:58:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-17: Introduced in Senate
- 2025-01-17 - IntroReferral: Introduced in Senate
- 2025-01-17 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-17: Introduced in Senate

## Actions

- 2025-01-17 - IntroReferral: Introduced in Senate
- 2025-01-17 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-17",
    "latestAction": {
      "actionDate": "2025-01-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/150",
    "number": "150",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000377",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Kelly, Mark [D-AZ]",
        "lastName": "Kelly",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Combating Cartels on Social Media Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:58:13Z",
    "updateDateIncludingText": "2025-12-05T21:58:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-17",
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
      "actionDate": "2025-01-17",
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
        "item": {
          "date": "2025-01-17T16:15:20Z",
          "name": "Referred To"
        }
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-17",
      "state": "OK"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-17",
      "state": "NC"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-01-17",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s150is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 150\nIN THE SENATE OF THE UNITED STATES\nJanuary 17, 2025 Mr. Kelly (for himself, Mr. Lankford , Mr. Tillis , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the Secretary of Homeland Security and the Secretary of State to implement a strategy to combat the efforts of transnational criminal organizations to recruit individuals in the United States via social media platforms and other online services and assess their use of such platforms and services for illicit activities.\n#### 1. Short title\nThis Act may be cited as the Combating Cartels on Social Media Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs, the Committee on the Judiciary, and the Committee on Foreign Relations of the Senate; and\n**(B)**\nthe Committee on Homeland Security, the Committee on the Judiciary, and the Committee on Foreign Affairs of the House of Representatives.\n**(2) Covered operator**\nThe term covered operator means the operator, developer, or publisher of a covered service.\n**(3) Covered service**\nThe term covered service means\u2014\n**(A)**\na social media platform;\n**(B)**\na mobile or desktop service with direct or group messaging capabilities, but not including text messaging services without other substantial social functionalities or electronic mail services, that the Secretary of Homeland Security determines is being or has been used by transnational criminal organizations in connection with matters described in section 3; or\n**(C)**\na digital platform, or an electronic application utilizing the digital platform, involving real-time interactive communication between multiple individuals, including multi-player gaming services and immersive technology platforms or applications, that the Secretary of Homeland Security determines is being or has been used by transnational criminal organizations in connection with matters described in section 3.\n**(4) Criminal enterprise**\nThe term criminal enterprise has the meaning given the term continuing criminal enterprise in section 408 of the Controlled Substances Act ( 21 U.S.C. 848 ).\n**(5) Illicit activities**\nThe term illicit activities means the following criminal activities that transcend national borders:\n**(A)**\nA violation of section 401 of the Controlled Substances Act ( 21 U.S.C. 841 ).\n**(B)**\nNarcotics trafficking, as defined in section 808 of the Foreign Narcotics Kingpin Designation Act ( 21 U.S.C. 1907 ).\n**(C)**\nWeapons trafficking.\n**(D)**\nMigrant smuggling, defined as a violation of section 274(a)(1)(A)(ii) of the Immigration and Nationality Act ( 8 U.S.C. 1324(a)(1)(A)(ii) ).\n**(E)**\nHuman trafficking, defined as\u2014\n**(i)**\na violation of section 1590, 1591, or 1592 of title 18, United States Code; or\n**(ii)**\nengaging in severe forms of trafficking in persons, as defined in section 103 of the Victims of Trafficking and Violence Protection Act of 2000 ( 22 U.S.C. 7102 ).\n**(F)**\nCyber crime, defined as a violation of section 1030 of title 18, United States Code.\n**(G)**\nA violation of any provision that is subject to intellectual property enforcement, as defined in section 302 of the Prioritizing Resources and Organization for Intellectual Property Act of 2008 ( 15 U.S.C. 8112 ).\n**(H)**\nBulk cash smuggling of currency, defined as a violation of section 5332 of title 31, United States Code.\n**(I)**\nLaundering the proceeds of the criminal activities described in subparagraphs (A) through (H).\n**(6) Transnational criminal organization**\nThe term transnational criminal organization means a group, or network, and associated individuals, that operate transnationally for the purposes of obtaining power, influence, or monetary or commercial gain, wholly or in part by certain unlawful means, while advancing their activities through a pattern of crime, corruption, or violence, and while protecting their unlawful activities through a transnational organizational structure and the exploitation of public corruption or transnational logistics, financial, or communication mechanisms.\n#### 3. Assessment of illicit usage\nNot later than 180 days after the date of enactment of this Act, the Secretary of Homeland Security, the Attorney General, and the Secretary of State shall submit to the appropriate congressional committees a joint assessment describing\u2014\n**(1)**\nthe use of covered services by transnational criminal organizations, or criminal enterprises acting on behalf of transnational criminal organizations, to engage in recruitment efforts, including the recruitment of individuals located in the United States, to engage in or provide support with respect to illicit activities occurring in the United States, Mexico, or otherwise in proximity to an international border of the United States;\n**(2)**\nthe use of covered services by transnational criminal organizations, or criminal enterprises acting on behalf of transnational criminal organizations, to engage in illicit activities or conduct in support of illicit activities, including\u2014\n**(A)**\nsmuggling or trafficking involving narcotics, other controlled substances, precursors thereof, or other items prohibited under the laws of the United States, Mexico, or another relevant jurisdiction, including firearms;\n**(B)**\nhuman smuggling or trafficking, with a particular focus on the exploitation of children; and\n**(C)**\ntransportation of bulk currency or monetary instruments in furtherance of smuggling or trafficking; and\n**(3)**\nthe existing efforts of the Secretary of Homeland Security, the Attorney General, the Secretary of State, and relevant government and law enforcement entities to counter, monitor, or otherwise respond to the usage of covered services described in paragraphs (1) and (2).\n#### 4. Strategy to combat cartel recruitment on social media and online platforms\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Homeland Security, the Attorney General, and the Secretary of State shall submit to the appropriate congressional committees a joint strategy, to be known as the National Strategy to Combat Illicit Recruitment Activity by Transnational Criminal Organizations on Social Media and Online Platforms , to combat the use of covered services by transnational criminal organizations, or criminal enterprises acting on behalf of transnational criminal organizations, to recruit individuals located in the United States to engage in or provide support for unlawful activities occurring in the United States, Mexico, or otherwise in proximity to an international border of the United States.\n##### (b) Elements\n**(1) In general**\nThe strategy required under subsection (a) shall, at a minimum, include the following:\n**(A)**\nA proposal to improve cooperation between the Secretary of Homeland Security, the Attorney General, the Secretary of State, and relevant law enforcement entities.\n**(B)**\nRecommendations to implement a process for the voluntary reporting of information regarding the recruitment efforts of transnational criminal organizations, or criminal enterprises acting on behalf of transnational criminal organizations, in the United States involving covered services.\n**(C)**\nA proposal to improve intragovernmental coordination with respect to the matters described in subsection (a), including between the Department of Homeland Security, the Department of Justice, the Department of State, and State, Tribal, and local governments.\n**(D)**\nA proposal to improve coordination within the Department of Homeland Security, the Department of Justice, and the Department of State and between the components of those Departments with respect to the matters described in subsection (a).\n**(E)**\nActivities to facilitate increased intelligence analysis for law enforcement purposes of efforts of transnational criminal organizations, or criminal enterprises acting on behalf of transnational criminal organizations, to utilize covered services for recruitment to engage in or provide support with respect to illicit activities.\n**(F)**\nActivities to foster international partnerships and enhance collaboration with foreign governments and, as applicable, multilateral institutions, with respect to the matters described in subsection (a).\n**(G)**\nActivities to specifically increase engagement and outreach with youth in border communities, including regarding the recruitment tactics of transnational criminal organizations, or criminal enterprises acting on behalf of transnational criminal organizations, and the consequences of participation in illicit activities.\n**(H)**\nA detailed description of the measures used to ensure\u2014\n**(i)**\nlaw enforcement and intelligence activities focus on the recruitment activities of transitional criminal organizations, or criminal enterprises acting on behalf of transnational criminal organizations, rather than individuals the transnational criminal organizations or enterprises attempt to or successfully recruit; and\n**(ii)**\nthe protection of privacy rights, civil rights, and civil liberties in carrying out the activities described in clause (i), with a particular focus on the protections in place to protect minors and constitutionally protected activities.\n**(2) Limitation**\nThe strategy required under subsection (a) shall not include legislative recommendations or elements predicated on the passage of legislation that is not enacted as of the date on which the strategy is submitted under subsection (a).\n##### (c) Consultation\nIn drafting and implementing the strategy required under subsection (a), the Secretary of Homeland Security, the Attorney General, and the Secretary of State shall, at a minimum, consult and engage with\u2014\n**(1)**\nthe heads of relevant components of the Department of Homeland Security, including\u2014\n**(A)**\nthe Under Secretary for Intelligence and Analysis;\n**(B)**\nthe Under Secretary for Strategy, Policy, and Plans;\n**(C)**\nthe Under Secretary for Science and Technology;\n**(D)**\nthe Commissioner of U.S. Customs and Border Protection;\n**(E)**\nthe Director of U.S. Immigration and Customs Enforcement;\n**(F)**\nthe Officer for Civil Rights and Civil Liberties;\n**(G)**\nthe Privacy Officer; and\n**(H)**\nthe Assistant Secretary of the Office for State and Local Law Enforcement;\n**(2)**\nthe heads of relevant components of the Department of Justice, including\u2014\n**(A)**\nthe Assistant Attorney General for the Criminal Division;\n**(B)**\nthe Assistant Attorney General for National Security;\n**(C)**\nthe Assistant Attorney General for the Civil Rights Division;\n**(D)**\nthe Chief Privacy and Civil Liberties Officer;\n**(E)**\nthe Director of the Organized Crime Drug Enforcement Task Forces;\n**(F)**\nthe Director of the Federal Bureau of Investigation; and\n**(G)**\nthe Director of the Bureau of Alcohol, Tobacco, Firearms, and Explosives;\n**(3)**\nthe heads of relevant components of the Department of State, including\u2014\n**(A)**\nthe Assistant Secretary for International Narcotics and Law Enforcement Affairs;\n**(B)**\nthe Assistant Secretary for Western Hemisphere Affairs; and\n**(C)**\nthe Coordinator of the Global Engagement Center;\n**(4)**\nthe Secretary of Health and Human Services;\n**(5)**\nthe Secretary of Education; and\n**(6)**\nas selected by the Secretary of Homeland Security, or his or her designee in the Office of Public Engagement, representatives of border communities, including representatives of\u2014\n**(A)**\nState, Tribal, and local governments, including school districts and local law enforcement; and\n**(B)**\nnongovernmental experts in the fields of\u2014\n**(i)**\ncivil rights and civil liberties;\n**(ii)**\nonline privacy;\n**(iii)**\nhumanitarian assistance for migrants; and\n**(iv)**\nyouth outreach and rehabilitation.\n##### (d) Implementation\n**(1) In general**\nNot later than 90 days after the date on which the strategy required under subsection (a) is submitted to the appropriate congressional committees, the Secretary of Homeland Security, the Attorney General, and the Secretary of State shall commence implementation of the strategy.\n**(2) Report**\n**(A) In general**\nNot later than 180 days after the date on which the strategy required under subsection (a) is implemented under paragraph (1), and semiannually thereafter for 5 years, the Secretary of Homeland Security, the Attorney General, and the Secretary of State shall submit to the appropriate congressional committees a joint report describing the efforts of the Secretary of Homeland Security, the Attorney General, and the Secretary of State, respectively, to implement the strategy required under subsection (a) and the progress of those efforts, which shall include a description of\u2014\n**(i)**\nthe recommendations, and corresponding implementation of those recommendations, with respect to the matters described in subsection (b)(1)(B);\n**(ii)**\nthe interagency posture with respect to the matters covered by the strategy required under subsection (a), which shall include a description of collaboration between the Secretary of Homeland Security, the Attorney General, the Secretary of State, other Federal entities, State, local, and Tribal entities, foreign governments, and, as applicable, multilateral institutions; and\n**(iii)**\nthe threat landscape, including new developments related to the recruitment efforts of transnational criminal organizations, or criminal enterprises acting on behalf of transnational criminal organizations, and the use by such organizations or enterprises of new or emergent covered services and recruitment methods.\n**(B) Form**\nEach report required under subparagraph (A) shall be submitted in unclassified form, but may contain a classified annex.\n**(3) Civil rights, civil liberties, and privacy assessment**\nNot later than 2 years after the date on which the strategy required under subsection (a) is implemented under paragraph (1), the Office for Civil Rights and Civil Liberties and the Privacy Office of the Department of Homeland Security, in consultation with the Assistant Attorney General for the Civil Rights Division and the Chief Privacy and Civil Liberties Officer of the Department of Justice, shall submit to the appropriate congressional committees a joint report that includes\u2014\n**(A)**\na detailed assessment of the measures used to ensure the protection of civil rights, civil liberties, and privacy rights in carrying out this section; and\n**(B)**\nrecommendations to improve the implementation of the strategy required under subsection (a).\n**(4) Rulemaking**\nPrior to implementation of the strategy required under subsection (a) at the Department of Homeland Security, the Secretary of Homeland Security shall issue rules to carry out this section in accordance with section 553 of title 5, United States Code.\n#### 5. Rule of construction\nNothing in this Act may be construed to expand the statutory law enforcement or regulatory authority of the Department of Homeland Security, the Department of Justice, or the Department of State.\n#### 6. No additional funds\nNo additional funds are authorized to be appropriated for the purpose of carrying out this Act.",
      "versionDate": "2025-01-17",
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
        "actionDate": "2025-01-16",
        "text": "Referred to the Subcommittee on Counterterrorism and Intelligence."
      },
      "number": "488",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Combating Cartels on Social Media Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computer security and identity theft",
            "updateDate": "2025-03-03T17:35:51Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-03T17:35:51Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-03-03T17:35:51Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-03-03T17:35:51Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-03-03T17:35:51Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2025-03-03T17:35:51Z"
          },
          {
            "name": "Intellectual property",
            "updateDate": "2025-03-03T17:35:51Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-03-03T17:35:51Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-03-03T17:35:51Z"
          },
          {
            "name": "Organized crime",
            "updateDate": "2025-03-03T17:35:51Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2025-03-03T17:35:51Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2025-03-03T17:35:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-21T16:18:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-17",
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
          "measure-id": "id119s150",
          "measure-number": "150",
          "measure-type": "s",
          "orig-publish-date": "2025-01-17",
          "originChamber": "SENATE",
          "update-date": "2025-07-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s150v00",
            "update-date": "2025-07-21"
          },
          "action-date": "2025-01-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Combating Cartels on Social Media Act of 2025</strong></p><p>This bill requires\u00a0the Departments of Homeland Security, Justice, and State to combat the use of social media by transnational criminal organizations to recruit individuals in the United States for illicit activities.\u00a0</p><p>Specifically, the departments must\u00a0jointly assess and implement a strategy to combat the use of social media platforms, messaging services, and other interactive digital platforms by these organizations to recruit individuals to engage in or support unlawful activities in the United States, Mexico, or otherwise near a U.S. international border.</p>"
        },
        "title": "Combating Cartels on Social Media Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s150.xml",
    "summary": {
      "actionDate": "2025-01-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Combating Cartels on Social Media Act of 2025</strong></p><p>This bill requires\u00a0the Departments of Homeland Security, Justice, and State to combat the use of social media by transnational criminal organizations to recruit individuals in the United States for illicit activities.\u00a0</p><p>Specifically, the departments must\u00a0jointly assess and implement a strategy to combat the use of social media platforms, messaging services, and other interactive digital platforms by these organizations to recruit individuals to engage in or support unlawful activities in the United States, Mexico, or otherwise near a U.S. international border.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119s150"
    },
    "title": "Combating Cartels on Social Media Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Combating Cartels on Social Media Act of 2025</strong></p><p>This bill requires\u00a0the Departments of Homeland Security, Justice, and State to combat the use of social media by transnational criminal organizations to recruit individuals in the United States for illicit activities.\u00a0</p><p>Specifically, the departments must\u00a0jointly assess and implement a strategy to combat the use of social media platforms, messaging services, and other interactive digital platforms by these organizations to recruit individuals to engage in or support unlawful activities in the United States, Mexico, or otherwise near a U.S. international border.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119s150"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s150is.xml"
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
      "title": "Combating Cartels on Social Media Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Combating Cartels on Social Media Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Homeland Security and the Secretary of State to implement a strategy to combat the efforts of transnational criminal organizations to recruit individuals in the United States via social media platforms and other online services and assess their use of such platforms and services for illicit activities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:23Z"
    }
  ]
}
```
