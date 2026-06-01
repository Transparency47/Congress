# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1274?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1274
- Title: PROTECT Our Children Reauthorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1274
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2026-01-30T16:15:47Z
- Update date including text: 2026-01-30T16:15:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1274",
    "number": "1274",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000797",
        "district": "25",
        "firstName": "Debbie",
        "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
        "lastName": "Wasserman Schultz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "PROTECT Our Children Reauthorization Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-30T16:15:47Z",
    "updateDateIncludingText": "2026-01-30T16:15:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:01:35Z",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NJ"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WV"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1274ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1274\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Ms. Wasserman Schultz (for herself, Mr. Van Drew , Mr. Moskowitz , and Mr. Moran ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo reauthorize the PROTECT Our Children Act of 2008, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the PROTECT Our Children Reauthorization Act of 2025 .\n#### 2. Reauthorization\n##### (a) Establishment of National Strategy for Child Exploitation Prevention and Interdiction\nSection 101 of the PROTECT Our Children Act of 2008 ( 34 U.S.C. 21111 ) is amended\u2014\n**(1)**\nin subsection (b), by striking every second year and inserting every fourth year ; and\n**(2)**\nby striking subsection (c) and inserting the following:\n(c) Required contents of National Strategy The National Strategy established under subsection (a) shall include the following: (1) An analysis of current trends, challenges, and the overall magnitude of the threat of child exploitation. (2) An analysis of future trends and challenges, including new technologies, that will impact the efforts to combat child exploitation. (3) Goals and strategic solutions to prevent and interdict child exploitation, including\u2014 (A) plans for interagency coordination; (B) engagement with the judicial branches of the Federal Government and State governments; (C) legislative recommendations for combating child exploitation; (D) cooperation with international, State, local, and Tribal law enforcement agencies; and (E) engagement with the private sector and other entities involved in efforts to combat child exploitation. (4) An analysis of Federal efforts dedicated to combating child exploitation, including\u2014 (A) a review of the policies and work of the Department of Justice and other Federal programs relating to the prevention and interdiction of child exploitation crimes, including training programs, and investigative and prosecution activity; and (B) a description of the efforts of the Department of Justice to cooperate and coordinate with, and provide technical assistance and support to, international, State, local, and Tribal law enforcement agencies and private sector and nonprofit entities with respect to child exploitation prevention and interdiction efforts. (5) An estimate of the resources required to effectively respond to child exploitation crimes at scale by\u2014 (A) each ICAC task force; (B) the Federal Bureau of Investigation, including investigators, forensic interviewers, and analysts of victims, witnesses, and forensics; (C) Homeland Security Investigations, including forensic interviewers and analysts of victims, witnesses, and forensics; (D) the United States Marshals Service; (E) the United States Secret Service; (F) the United States Postal Service; (G) the criminal investigative offices of the Department of Defense; and (H) any component of an agency described in this paragraph; (6) A review of the Internet Crimes Against Children Task Force Program, including\u2014 (A) the number of ICAC task forces and the location of each ICAC task force; (B) the number of trained personnel at each ICAC task force; (C) the amount of Federal grants awarded to each ICAC task force; and (D) an assessment of the Federal, State, and local cooperation with respect to each ICAC task force, including\u2014 (i) the number of arrests made by each ICAC task force; (ii) the number of criminal referrals to United States attorneys for prosecution; (iii) the number of prosecutions and convictions from the referrals described in clause (ii); (iv) the number, if available, of local prosecutions and convictions based on ICAC task force investigations; and (v) any other information determined by the Attorney General demonstrating the level of Federal, State, Tribal, and local coordination and cooperation. (7) An assessment of training needs for each ICAC task force and affiliated agencies. (8) An assessment of Federal investigative and prosecution activity relating to reported incidents of child exploitation crimes that include a number of factors, including\u2014 (A) the number of investigations, arrests, prosecutions and convictions for a crime of child exploitation; and (B) the average sentence imposed and the statutory maximum sentence that could be imposed for each crime of child exploitation. (9) A review of all available statistical data indicating the overall magnitude of child pornography trafficking in the United States and internationally, including\u2014 (A) the number of foreign and domestic suspects observed engaging in accessing and sharing child pornography; (B) the number of tips or other statistical data from the CyberTipline of the National Center for Missing and Exploited Children and other data indicating the magnitude of child pornography trafficking; and (C) any other statistical data indicating the type, nature, and extent of child exploitation crime in the United States and abroad. .\n##### (b) Establishment of National ICAC Task Force Program\nSection 102 of the PROTECT Our Children Act of 2008 ( 34 U.S.C. 21112 ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nby inserting , Tribal, military, after State ; and\n**(B)**\nby striking and child obscenity and pornography cases and inserting child obscenity and pornography cases, and the identification of child victims ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2), by striking consult with and consider and all that follows through track record of success. and inserting , evaluate the task forces funded under the ICAC Task Force Program to determine if those task forces are operating in an effective manner. ;\n**(B)**\nin paragraph (3)(B)\u2014\n**(i)**\nby striking establish a new task force and inserting establish a new or continue an existing task force ; and\n**(ii)**\nby striking state and inserting State ; and\n**(C)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (A), by striking may and inserting shall ;\n**(ii)**\nby striking subparagraph (B); and\n**(iii)**\nby redesignating subparagraph (C) as subparagraph (B); and\n**(3)**\nby adding at the end the following:\n(c) Limited liability for ICAC task forces (1) In general Except as provided in paragraph (2), a civil claim or criminal charge against an ICAC task force established pursuant to this section and sections 103 and 104, including any law enforcement agency that participates on such a task force or a director, officer, employee, or agent of such a law enforcement agency, arising from the prioritization decisions with respect to leads related to internet crimes against children described in section 104(8), may not be brought in any Federal or State court. (2) Intentional, reckless, or other misconduct Paragraph (1) shall not apply to a claim if the ICAC task force or law enforcement agency, or a director, officer, employee, or agent of that law enforcement agency\u2014 (A) engaged in intentional misconduct; or (B) acted, or failed to act\u2014 (i) with actual malice; (ii) with reckless disregard to a substantial risk of causing physical injury without legal justification; or (iii) for a purpose unrelated to the performance of any responsibility or function under section 104(8). .\n##### (c) Purpose of ICAC task forces\nSection 103 of the PROTECT Our Children Act of 2008 ( 34 U.S.C. 21113 ) is amended\u2014\n**(1)**\nin paragraph (1), by inserting , and the identification of child victims of those crimes before the semicolon at the end;\n**(2)**\nin paragraph (2), by inserting and prioritizing investigations that task force personnel, through the background, training and experience of those personnel and the consideration of all relevant circumstances, determine to be most likely to result in positive case outcomes and in the rescue of children before the semicolon at the end;\n**(3)**\nin paragraph (3)\u2014\n**(A)**\nby striking and local law enforcement and inserting Tribal, military, and local law enforcement ; and\n**(B)**\nby inserting , including probation and parole agencies, child advocacy centers, and child protective services, after agencies ;\n**(4)**\nin paragraph (8), by striking and at the end;\n**(5)**\nin paragraph (9), by striking the period at the end and inserting ; and ; and\n**(6)**\nby adding at the end the following:\n(10) educating the judiciary on\u2014 (A) the link between intrafamilial contact offenses and technology-facilitated crimes; and (B) characteristics of internet offenders, including the interest of online offenders in incest-themed material, sadism, and other related paraphilias or illegal activity. .\n##### (d) Duties and functions of task forces\nSection 104 of the PROTECT Our Children Act of 2008 ( 34 U.S.C. 21114 ) is amended\u2014\n**(1)**\nin paragraph (3)\u2014\n**(A)**\nby inserting reactive and before proactive ;\n**(B)**\nby inserting conduct digital before forensic examinations ; and\n**(C)**\nby inserting engage in before effective prosecutions ;\n**(2)**\nby striking paragraph (8) and inserting the following:\n(8) investigate, seek prosecution with respect to, and identify child victims from leads relating to Internet crimes against children, including CyberTipline reports, with prioritization determined according to circumstances and by each task force, as described in section 102; ;\n**(3)**\nby striking paragraph (9); and\n**(4)**\nby redesignating paragraphs (10) and (11) as paragraphs (9) and (10), respectively.\n##### (e) National Internet Crimes Against Children Data System\nSection 105 of the PROTECT Our Children Act of 2008 ( 34 U.S.C. 21115 ) is amended\u2014\n**(1)**\nin subsection (a), by striking shall establish and inserting may establish ;\n**(2)**\nin subsection (b) by striking continue and build upon Operation Fairplay developed by the Wyoming Attorney General\u2019s office, which has established a secure, dynamic undercover infrastructure that has facilitated and inserting facilitate ; and\n**(3)**\nin subsection (g)\u2014\n**(A)**\nby striking paragraph (3);\n**(B)**\nby redesignating paragraphs (4) through (8) as paragraphs (3) through (7), respectively; and\n**(C)**\nin paragraph (7), as so redesignated, by striking 1 representative and inserting 2 representatives .\n##### (f) ICAC grant program\nSection 106 of the PROTECT Our Children Act of 2008 ( 34 U.S.C. 21116 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2)(B)(ii)(II), by striking Operation Fairplay, ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nby striking subparagraph (A) and inserting the following:\n(A) Not less than 20 percent of the total funds appropriated to carry out this section shall be distributed to support the ICAC Task Force Program through grants to\u2014 (i) provide training and technical assistance to members of the ICAC Task Force Program; (ii) maintain, enhance, research, and develop tools and technology to assist members of the ICAC Task Force Program; (iii) provide other support to the ICAC Task Force Program determined by the Attorney General; (iv) conduct research; (v) support the annual National Law Enforcement Training on Child Exploitation of the Office of Juvenile Justice and Delinquency Prevention; and (vi) provide wellness training. ; and\n**(2)**\nin subsection (d)(1)\u2014\n**(A)**\nin subparagraph (B)\u2014\n**(i)**\nin clause (ii), by striking and at the end;\n**(ii)**\nin clause (iii), by striking , including and all that follows through such crime under State law. and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(iv) the number of child victims identified. ;\n**(B)**\nby striking subparagraph (D); and\n**(C)**\nby redesignating subparagraphs (E) through (G) as subparagraphs (D) through (F), respectively.\n##### (g) Authorization of appropriations\nSection 107(a) of the PROTECT Our Children Act of 2008 ( 34 U.S.C. 21117(a) ) is amended\u2014\n**(1)**\nin paragraph (9), by striking and at the end;\n**(2)**\nin paragraph (10), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(11) $70,000,000 for fiscal year 2026; (12) $80,000,000 for fiscal year 2027; and (13) $90,000,000 for fiscal year 2028. .\n##### (h) Additional regional computer forensic labs\nThe PROTECT Our Children Act of 2008 ( 34 U.S.C. 21101 et seq. ) is amended by striking title II.\n##### (i) Reporting requirements of providers\nSection 2258A(c) of title 18, United States Code, is amended, in the matter preceding paragraph (1), by inserting and all supplemental data included in the report after each report made under subsection (a)(1) .",
      "versionDate": "2025-02-12",
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
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-20",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 80."
      },
      "number": "539",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PROTECT Our Children Reauthorization Act of 2025",
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
            "name": "Child safety and welfare",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Crime prevention",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Crimes against children",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Criminal justice information and records",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Domestic violence and child abuse",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Missing persons",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Pornography",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-06-02T20:13:32Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2025-06-02T20:13:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-17T14:48:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
    "originChamber": "House",
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
          "measure-id": "id119hr1274",
          "measure-number": "1274",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2026-01-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1274v00",
            "update-date": "2026-01-30"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>PROTECT Our Children Reauthorization Act of 2025</strong><br/>\u00a0<br/>This bill reauthorizes through FY2028 and updates (1) the National Strategy for Child Exploitation Prevention and Interdiction (National Strategy), and (2) the National Internet Crimes Against Children (ICAC) Task Force Program.</p><p>With respect to the National Strategy, current law requires the Department of Justice (DOJ) to update the strategy every two years and include 19 specific elements in the strategy (e.g., long-range goals, annual measurable objectives, and future trends). This bill requires DOJ to update the National Strategy every four years. The bill also revises and consolidates the 19 required elements into 9 required elements, including an analysis of current trends and challenges as well as the overall magnitude of the threat of child exploitation.</p><p>The ICAC Task Force Program is a national network of task forces that support state and local efforts to investigate and prosecute the online sexual exploitation of children. This bill requires ICAC task forces to increase the investigative capacity of law enforcement to identify child victims and report the number of child victims identified in their annual reports. The bill also limits the liability of ICAC task forces for civil claims or criminal charges in federal or state court arising from decisions with respect to leads related to internet crimes against children.</p><p>Finally, the bill requires the National Center for Missing & Exploited Children to provide additional information to law enforcement agencies when it refers a report of online sexual exploitation of children for investigation.\u00a0</p>"
        },
        "title": "PROTECT Our Children Reauthorization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1274.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>PROTECT Our Children Reauthorization Act of 2025</strong><br/>\u00a0<br/>This bill reauthorizes through FY2028 and updates (1) the National Strategy for Child Exploitation Prevention and Interdiction (National Strategy), and (2) the National Internet Crimes Against Children (ICAC) Task Force Program.</p><p>With respect to the National Strategy, current law requires the Department of Justice (DOJ) to update the strategy every two years and include 19 specific elements in the strategy (e.g., long-range goals, annual measurable objectives, and future trends). This bill requires DOJ to update the National Strategy every four years. The bill also revises and consolidates the 19 required elements into 9 required elements, including an analysis of current trends and challenges as well as the overall magnitude of the threat of child exploitation.</p><p>The ICAC Task Force Program is a national network of task forces that support state and local efforts to investigate and prosecute the online sexual exploitation of children. This bill requires ICAC task forces to increase the investigative capacity of law enforcement to identify child victims and report the number of child victims identified in their annual reports. The bill also limits the liability of ICAC task forces for civil claims or criminal charges in federal or state court arising from decisions with respect to leads related to internet crimes against children.</p><p>Finally, the bill requires the National Center for Missing & Exploited Children to provide additional information to law enforcement agencies when it refers a report of online sexual exploitation of children for investigation.\u00a0</p>",
      "updateDate": "2026-01-30",
      "versionCode": "id119hr1274"
    },
    "title": "PROTECT Our Children Reauthorization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>PROTECT Our Children Reauthorization Act of 2025</strong><br/>\u00a0<br/>This bill reauthorizes through FY2028 and updates (1) the National Strategy for Child Exploitation Prevention and Interdiction (National Strategy), and (2) the National Internet Crimes Against Children (ICAC) Task Force Program.</p><p>With respect to the National Strategy, current law requires the Department of Justice (DOJ) to update the strategy every two years and include 19 specific elements in the strategy (e.g., long-range goals, annual measurable objectives, and future trends). This bill requires DOJ to update the National Strategy every four years. The bill also revises and consolidates the 19 required elements into 9 required elements, including an analysis of current trends and challenges as well as the overall magnitude of the threat of child exploitation.</p><p>The ICAC Task Force Program is a national network of task forces that support state and local efforts to investigate and prosecute the online sexual exploitation of children. This bill requires ICAC task forces to increase the investigative capacity of law enforcement to identify child victims and report the number of child victims identified in their annual reports. The bill also limits the liability of ICAC task forces for civil claims or criminal charges in federal or state court arising from decisions with respect to leads related to internet crimes against children.</p><p>Finally, the bill requires the National Center for Missing & Exploited Children to provide additional information to law enforcement agencies when it refers a report of online sexual exploitation of children for investigation.\u00a0</p>",
      "updateDate": "2026-01-30",
      "versionCode": "id119hr1274"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1274ih.xml"
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
      "title": "PROTECT Our Children Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T11:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROTECT Our Children Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T11:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize the PROTECT Our Children Act of 2008, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T11:03:24Z"
    }
  ]
}
```
