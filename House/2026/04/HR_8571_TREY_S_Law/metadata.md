# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8571?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8571
- Title: TREY'S Law
- Congress: 119
- Bill type: HR
- Bill number: 8571
- Origin chamber: House
- Introduced date: 2026-04-29
- Update date: 2026-05-19T19:46:12Z
- Update date including text: 2026-05-19T19:46:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-29: Introduced in House

## Actions

- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8571",
    "number": "8571",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "G000603",
        "district": "26",
        "firstName": "Brandon",
        "fullName": "Rep. Gill, Brandon [R-TX-26]",
        "lastName": "Gill",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "TREY'S Law",
    "type": "HR",
    "updateDate": "2026-05-19T19:46:12Z",
    "updateDateIncludingText": "2026-05-19T19:46:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-29",
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
          "date": "2026-04-29T13:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "TX"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "TX"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "SC"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "TX"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "TX"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8571ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8571\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2026 Mr. Gill of Texas (for himself, Ms. Johnson of Texas , Mr. Self , Ms. Mace , Mr. Gooden , and Mr. Hunt ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit the enforcement of certain contractual clauses that restrict disclosure of sexual abuse of minors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Terminating Restrictive Enforcement of Youth Settlements Law or TREY'S Law .\n#### 2. Findings and purposes\n##### (a) Findings\n**(1) Instrumentalities of interstate commerce**\nCongress finds the following:\n**(A)**\nSexual abuse of minors, including abuse facilitated through instrumentalities of interstate commerce, is a matter of national concern.\n**(B)**\nAgreements containing nondisclosure and confidentiality provisions, frequently concluded through the instrumentalities of interstate commerce, have been used to silence survivors of sexual abuse and conceal ongoing or repeated abuse.\n**(C)**\nThe enforcement of such provisions interferes with reporting to law enforcement agencies, child protection authorities, Federal regulators, Members of Congress, and the courts, and frustrates the enforcement of Federal criminal and civil law.\n**(2) Necessary and proper clause and enforcement of Federal criminal law**\nCongress further finds the following:\n**(A)**\nSexual abuse and trafficking of minors are prohibited under Federal criminal law, including chapter 110 of title 18, United States Code, and section 1591 of title 18, United States Code.\n**(B)**\nNondisclosure and confidentiality agreements that prohibit or restrict disclosure of sexual abuse of a minor interfere with reporting to law enforcement, child protection authorities, courts, Federal regulators, and Members of Congress.\n**(C)**\nSuch agreements frustrate the investigation and prosecution of Federal crimes, chill cooperation with law enforcement, and function as private mechanisms to obstruct justice.\n**(D)**\nCongress has authority under clause 18 of section 8 of article I of the Constitution of the United States (commonly known as the Necessary and Proper Clause ) to ensure that private agreements are not used to impede the enforcement of Federal criminal and civil law protecting minors from sexual exploitation and abuse.\n**(3) State action and section 5 of the 14th Amendment**\nCongress further finds the following:\n**(A)**\nSurvivors of child sexual abuse possess fundamental constitutional interests, secured by provisions of the Bill of Rights as incorporated against the States through the 14th Amendment to the Constitution of the United States, in reporting crimes, seeking redress through the courts, cooperating with law enforcement, and petitioning the government for protection and enforcement.\n**(B)**\nWhen State courts or other governmental authorities enforce nondisclosure or confidentiality provisions that prohibit or restrict disclosure of sexual abuse of a minor, such enforcement constitutes State action for purposes of the 14th Amendment to the Constitution of the United States.\n**(C)**\nJudicial enforcement of such provisions may deprive survivors of due process of law, equal protection of the laws, and meaningful access to courts, including rights derived from the First Amendment to the Constitution of the United States and incorporated against the States, in violation of the 14th Amendment.\n**(D)**\nAgreements that obstruct justice, suppress the reporting of crimes, or conceal criminal conduct have long been regarded at common law, including at the time of the founding of the United States, as void and unenforceable as against public policy, and fall outside the traditional scope of protected contractual liberty.\n**(E)**\nAt the time of the founding of the United States, private agreements purporting to suppress prosecution, conceal felonies, or restrain the reporting of crimes were not recognized as valid or enforceable contracts, and no party possessed a vested right in their judicial enforcement.\n**(F)**\nCongress has authority under section 5 of the 14th Amendment to the Constitution of the United States to enact appropriate remedial and preventive legislation to prevent and remedy constitutional violations arising from State judicial enforcement of private agreements that suppress disclosure of criminal conduct involving minors.\n##### (b) Purpose\nThe purpose of this Act is\u2014\n**(1)**\nto enforce the guarantees of the 14th Amendment to the Constitution of the United States, including the right to petition the government for redress of grievances and the right of access to courts, by preventing State courts and other governmental authorities from enforcing nondisclosure or confidentiality provisions that suppress disclosure of sexual abuse of minors;\n**(2)**\nto ensure, pursuant to the authority of Congress under article I of the Constitution of the United States, including the Necessary and Proper Clause, that private agreements are not used to obstruct the investigation or prosecution of Federal crimes involving the sexual abuse or trafficking of minors;\n**(3)**\nto preserve access to courts and the right to petition the government for redress of grievances; and\n**(4)**\nto ensure that survivors of sexual abuse of minors, and persons with knowledge of such abuse, may disclose such abuse freely and without fear of civil liability.\n#### 3. Definitions\nIn this Act:\n**(1) Minor person**\nThe term minor person means an individual who has not attained 18 years of age.\n**(2) Nondisclosure clause**\nThe term nondisclosure clause means a provision in a contract or agreement that prohibits 1 or more parties to the contract or agreement from disclosing conduct or information covered by the terms and conditions of the contract or agreement.\n**(3) Sexual abuse against a minor person**\nThe term sexual abuse against a minor person means\u2014\n**(A)**\nconduct that constitutes or allegedly constitutes\u2014\n**(i)**\nan offense under chapter 110 of title 18, United States Code; or\n**(ii)**\nsex trafficking of a minor person under section 1591 of title 18, United States Code; or\n**(B)**\nany sexual act or sexual contact involving a minor person that constitutes a criminal offense under Federal law or the law of the State in which the act or contact occurs.\n#### 4. Nondisclosure agreements void and unenforceable\n##### (a) In general\nA nondisclosure clause shall be void and unenforceable as against public policy only to the extent that the nondisclosure clause prohibits\u2014\n**(1)**\na victim or alleged victim of sexual abuse against a minor person from disclosing\u2014\n**(A)**\nthat act of sexual abuse against a minor person; or\n**(B)**\nfacts related to that act of sexual abuse against a minor person; or\n**(2)**\nany other person from disclosing facts related to sexual abuse against a minor person described in paragraph (1) in support of, in furtherance of, or consistent with the right of a victim or alleged victim to disclose under that paragraph.\n##### (b) Permissible confidentiality\nNothing in this section shall be construed to prohibit a person, including a victim or alleged victim of sexual abuse against a minor person, from entering into a contract or agreement that restricts the disclosure of information, including the amount or payment terms of a settlement, by another party to the contract or agreement, including an alleged perpetrator, so long as such restriction does not prevent disclosure protected under subsection (a).\n#### 5. Retroactive application\n##### (a) In general\nThis Act shall apply to any nondisclosure clause in a contract or agreement entered into before, on, or after the date of enactment of this Act.\n##### (b) No enforcement actions\nNo person may enforce or attempt to enforce a nondisclosure clause described in section 4(a), regardless of the date on which the contract or agreement containing the nondisclosure clause was entered into.\n##### (c) Preemption\n**(1) In general**\nThis Act supersedes any State law to the extent that such law permits enforcement of a provision, the enforcement of which is prohibited under this Act.\n**(2) Rule of construction**\nNothing in this Act shall be construed to prohibit a State or locality from enacting legislation that\u2014\n**(A)**\nis consistent with this Act; or\n**(B)**\nprovides greater protection to a victim of sexual abuse against a minor person than is provided under this Act.",
      "versionDate": "2026-04-29",
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
        "actionDate": "2026-05-14",
        "text": "Committee on the Judiciary. Ordered to be reported without amendment favorably."
      },
      "number": "3966",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "TREY'S Law",
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
        "name": "Law",
        "updateDate": "2026-05-19T19:46:11Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8571ih.xml"
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
      "title": "TREY'S Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TREY'S Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Terminating Restrictive Enforcement of Youth Settlements Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the enforcement of certain contractual clauses that restrict disclosure of sexual abuse of minors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:34Z"
    }
  ]
}
```
