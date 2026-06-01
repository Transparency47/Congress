# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4607?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4607
- Title: SEEK HELP Act
- Congress: 119
- Bill type: HR
- Bill number: 4607
- Origin chamber: House
- Introduced date: 2025-07-22
- Update date: 2026-03-07T22:41:20Z
- Update date including text: 2026-03-07T22:41:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-22: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-22: Introduced in House

## Actions

- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4607",
    "number": "4607",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "SEEK HELP Act",
    "type": "HR",
    "updateDate": "2026-03-07T22:41:20Z",
    "updateDateIncludingText": "2026-03-07T22:41:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-22",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-22",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T14:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-22T14:02:10Z",
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
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "WV"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "NE"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "CA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "NY"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4607ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4607\nIN THE HOUSE OF REPRESENTATIVES\nJuly 22, 2025 Mr. Neguse (for himself, Mrs. Miller of West Virginia , Ms. Dean of Pennsylvania , Mr. Bacon , Mr. Levin , and Ms. Tenney ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide protections from prosecution for drug possession to individuals who seek medical assistance when witnessing or experiencing an overdose, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Samaritan Efforts to Ensure Key Health Emergency and Life-saving Protections Act or the SEEK HELP Act .\n#### 2. Definitions\nIn this Act\u2014\n**(1)**\nthe term controlled substance has the meaning given that term in section 102 of the Controlled Substances Act ( 21 U.S.C. 802 );\n**(2)**\nthe term emergency response providers has the meaning given that term in section 2 of the Homeland Security Act of 2002 ( 6 U.S.C. 101 );\n**(3)**\nthe term opioid overdose reversal drug means a drug approved under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) that\u2014\n**(A)**\nis indicated for the partial or complete reversal of the pharmacological effects of an opioid overdose in the human body; and\n**(B)**\nhas moved in or affecting interstate or foreign commerce;\n**(4)**\nthe term Secretary means the Secretary of Health and Human Services; and\n**(5)**\nthe term seek medical assistance means\u2014\n**(A)**\nreporting a drug overdose or other medical emergency to a law enforcement authority, an emergency response provider, the 9\u20131\u20131 system, a poison control center, or a medical or drug treatment provider; or\n**(B)**\nassisting another individual who is making a report described in subparagraph (A).\n#### 3. Good Samaritan protections for drug overdose responses\n##### (a) Civil liability protections for administration of opioid overdose reversal drugs\n**(1) In general**\nExcept as provided in paragraph (2), an individual shall not be liable in a civil action in a Federal or State court for harm caused by the emergency administration of an opioid overdose reversal drug to another individual who is or reasonably appears to be suffering a drug overdose if the individual administers the opioid overdose reversal drug in good faith.\n**(2) Exceptions**\nParagraph (1) shall not apply with respect to harm caused by willful or criminal misconduct, gross negligence, reckless misconduct, or a conscious, flagrant indifference to the rights or safety of the victim who was harmed.\n**(3) Rule of construction**\nWith respect to a person who administers an opioid overdose reversal drug to another individual, this section supersedes the law of a State only to the extent that the State has no statute or regulation that provides such a person with immunity in a civil action for the use of an opioid overdose reversal drug, as described in paragraph (1).\n##### (b) Criminal liability protections for seeking medical assistance for an overdose\n**(1) Definition**\nIn this subsection, the term covered individual means an individual who\u2014\n**(A)**\nin good faith and a timely manner\u2014\n**(i)**\nseeks medical assistance for an individual experiencing or reasonably appears to be experiencing a drug overdose; or\n**(ii)**\nseeks medical assistance for himself or herself for a drug overdose; and\n**(B)**\ndid not seek the medical assistance during the course of the execution of an arrest warrant, search warrant, or other lawful search or seizure.\n**(2) Liability protection**\nA covered individual shall not be subject to prosecution, civil asset forfeiture, or revocation of supervised released under section 404 of the Controlled Substances Act ( 21 U.S.C. 844 ) for possession of a controlled substance if a law enforcement agency, or other government agency, is made aware of the possession solely based on the fact that the covered individual sought medical assistance as described in clause (i) or (ii) of paragraph (1)(A).\n**(3) Admissibility and seizure of evidence or contraband**\nNothing in this subsection shall be construed\u2014\n**(A)**\nto limit the admissibility of evidence in connection with the prosecution of\u2014\n**(i)**\nan offense with regard to an individual who does not qualify for the protections under paragraph (2); or\n**(ii)**\nan offense not described in paragraph (2) that is committed by an individual who qualifies for the protections under such paragraph;\n**(B)**\nto limit any seizure of evidence or contraband otherwise permitted by law; or\n**(C)**\nto limit the arrest of the individual or search and seizure of any evidence or contraband if there is an outstanding State or Federal warrant for the individual.\n##### (c) Public awareness campaign\nThe Secretary, in consultation with the Administrator of the Drug Enforcement Administration, shall carry out a public awareness campaign regarding the liability protections under this section.\n##### (d) Use of JAG funds\nSection 501(a)(1) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10152(a)(1) ) is amended by adding at the end the following:\n(J) Training programs for law enforcement officers of States and units of local government regarding legal protections for individuals seeking medical assistance in connection with a controlled substance overdose. .\n#### 4. Use of block grant funding for public awareness campaigns and initiatives\n##### (a) In general\nA State receiving a grant under section 1921 of the Public Health Service Act ( 42 U.S.C. 300x\u201321 ) may use amounts described in section 1922(a)(1) of such Act ( 42 U.S.C. 300x\u201322(a)(1) ) to\u2014\n**(1)**\nconduct a public awareness campaign regarding the overdose Good Samaritan law of the State;\n**(2)**\nprovide training to criminal justice professionals, stakeholders (including health care providers), emergency medical service providers, and the general public on applicable overdose Good Samaritan laws; and\n**(3)**\nto the extent possible, share data with the Secretary regarding the impact of overdose Good Samaritan laws of the State on individuals experiencing an overdose, which shall include the number of calls seeking medical assistance that were received by a law enforcement agency, the 9\u20131\u20131 system, a poison control center, or a medical or drug treatment providers for seeking medical assistance in the event of a drug overdose.\n##### (b) Definition\nIn this section, the term overdose Good Samaritan law means a statute providing protection from liability relating to seeking medical assistance in connection with a controlled substance overdose or administering an opioid overdose reversal drug.\n#### 5. GAO report to study effectiveness and implementation\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report on evaluating the implementation of Good Samaritan laws for drug overdose and the effectiveness of grant funding provided to States and localities for awareness campaigns related to those laws.\n##### (b) Contents\nThe report required under subsection (a) shall\u2014\n**(1)**\nassess the extent to which States and localities have implemented and enforced Good Samaritan laws for drug overdose;\n**(2)**\nevaluate the effectiveness of the laws described in paragraph (1) in encouraging the reporting of overdoses and the provision of timely medical assistance;\n**(3)**\nan estimate of the number of individuals impacted by the laws described in paragraph (1), including the number of individuals who have received legal protections or immunities under such laws;\n**(4)**\nanalyze the impact of the laws described in paragraph (1), including\u2014\n**(A)**\nan assessment of changes in overdose-related fatalities, emergency department visits, and the use of naloxone or other overdose reversal interventions; and\n**(B)**\ndata on the number of calls received for overdoses before and after the implementation of such laws;\n**(5)**\nevaluate the effectiveness of grant funding provided to States and localities for the purpose of spreading awareness about the laws described in paragraph (1);\n**(6)**\nassess the reach and impact of educational campaigns, community outreach initiatives, and training programs aimed at informing the public, healthcare providers, law enforcement personnel, and other relevant stakeholders about the protections and benefits provided by the laws described in paragraph (1);\n**(7)**\nidentify any barriers or challenges encountered during the implementation of the laws described in paragraph (1) and associated awareness campaigns, including\u2014\n**(A)**\nexamining the legal, logistical, resource-related, or cultural factors that may impede successful adoption and utilization of the laws; and\n**(B)**\nexploring any challenges faced by individuals seeking help or reporting overdoses due to potential legal repercussions;\n**(8)**\nhighlight any best practices identified in States and localities that have effectively implemented the laws described in paragraph (1) and conducted successful awareness campaigns, including recommendations on best methods for assessing and evaluating the implementation and success for Good Samaritan laws;\n**(9)**\nprovide recommendations for improving the implementation and impact of the laws described in paragraph (1) and optimizing the use of grant funding for education and outreach efforts; and\n**(10)**\nif multiple States or localities have implemented different variations of the laws described in paragraph (1), include a comparative analysis of their respective approaches identifying variations in outcomes, effectiveness, or challenges faced and providing insights for potential improvements or standardization of the laws.\n##### (c) Cooperation and access\nFederal agencies and relevant State and local authorities shall cooperate with the Comptroller General of the United States and provide access to necessary information and data to facilitate the completion of the report required under subsection (a).",
      "versionDate": "2025-07-22",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-17T15:37:58Z"
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
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4607ih.xml"
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
      "title": "SEEK HELP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SEEK HELP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Samaritan Efforts to Ensure Key Health Emergency and Life-saving Protections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide protections from prosecution for drug possession to individuals who seek medical assistance when witnessing or experiencing an overdose, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T07:48:50Z"
    }
  ]
}
```
