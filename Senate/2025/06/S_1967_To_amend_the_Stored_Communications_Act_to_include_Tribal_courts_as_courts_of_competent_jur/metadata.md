# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1967?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1967
- Title: PROTECT Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1967
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2026-03-13T19:16:57Z
- Update date including text: 2026-03-13T19:16:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1967",
    "number": "1967",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "PROTECT Act of 2025",
    "type": "S",
    "updateDate": "2026-03-13T19:16:57Z",
    "updateDateIncludingText": "2026-03-13T19:16:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Indian Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T16:57:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Indian Affairs Committee",
      "systemCode": "slia00",
      "type": "Other"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1967is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1967\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Mr. Daines (for himself and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Indian Affairs\nA BILL\nTo amend the Stored Communications Act to include Tribal courts as courts of competent jurisdiction, to amend the Indian Civil Rights Act of 1968 to confer Tribal jurisdiction over controlled substances, related offenses, and firearms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protection for Reservation Occupants against Trafficking and Evasive Communications Today Act of 2025 or the PROTECT Act of 2025 .\n#### 2. Tribal courts as courts of competent jurisdiction under Stored Communications Act\n##### (a) Definitions\nSection 2711 of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (B), by striking or at the end;\n**(B)**\nby redesignating subparagraph (C) as subparagraph (D); and\n**(C)**\nby inserting after subparagraph (B) the following:\n(C) a Tribal court; or ; and\n**(2)**\nby striking paragraph (4) and inserting the following:\n(4) the term governmental entity means a department or agency of\u2014 (A) the United States; (B) any State or political subdivision thereof; or (C) any Indian Tribe or political subdivision thereof; (5) the term Indian Tribe means any Indian or Alaska Native tribe, band, nation, pueblo, village, community, component band, or component reservation individually identified (including parenthetically) on the most recent list published by the Secretary of the Interior under section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ); and (6) the term Tribal court means a court of general criminal jurisdiction of an Indian Tribe authorized by the law of that Indian Tribe to issue search warrants. .\n##### (b) Required disclosure of customer communications or records\nSection 2703 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking the first sentence and inserting the following:\n(1) In storage 180 days or less A governmental entity may require the disclosure by a provider of electronic communication service of the contents of a wire or electronic communication, that is in electronic storage in an electronic communications system for 180 days or less, only pursuant to a warrant issued by a court of competent jurisdiction\u2014 (A) using the procedures described in the Federal Rules of Criminal Procedure; (B) in the case of a State court, using State warrant procedures; (C) in the case of a court-martial or other proceeding under chapter 47 of title 10 (the Uniform Code of Military Justice), under section 846 of that title, in accordance with regulations prescribed by the President; or (D) in the case of a Tribal court, using the warrant procedures described in section 202(a)(2) of Public Law 90\u2013284 (commonly known as the Indian Civil Rights Act of 1968 ) ( 25 U.S.C. 1302(a)(2) ). (2) In storage more than 180 days ;\n**(2)**\nin subsection (b)(1)\u2014\n**(A)**\nin subparagraph (A), by striking using the procedures described in the Federal Rules of Criminal Procedure and all that follows through prescribed by the President) and inserting in accordance with subsection (a)(1) ; and\n**(B)**\nin subparagraph (B)(i), by inserting , Tribal, after a Federal each place it appears; and\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(A), by striking using the procedures described in the Federal Rules of Criminal Procedure and all that follows through prescribed by the President) and inserting in accordance with subsection (a)(1) ; and\n**(B)**\nin paragraph (2), in the undesignated matter following subparagraph (F), by inserting , Tribal, after a Federal each place it appears.\n##### (c) Delayed notice\nSection 2705(a)(1)(B) of title 18, United States Code, is amended by inserting , Tribal, after a Federal each place it appears.\n##### (d) Civil action\nSection 2707(g) of title 18, United States Code, is amended, in the second sentence, by inserting Tribal, after State, .\n##### (e) Wrongful disclosure of video tape rental or sale records\nSection 2710 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (b)(2)(C), by inserting after an equivalent State warrant, the following: a warrant issued by a Tribal court using the warrant procedures described in section 202(a)(2) of Public Law 90\u2013284 (commonly known as the Indian Civil Rights Act of 1968 ) ( 25 U.S.C. 1302(a)(2) ), ; and\n**(2)**\nin subsection (d), by striking or a political subdivision of a State and inserting a political subdivision of a State, or an Indian Tribe .\n#### 3. Tribal jurisdiction over controlled substances, related offenses, and firearms\nSection 204 of Public Law 90\u2013284 (commonly known as the Indian Civil Rights Act of 1968 ) ( 25 U.S.C. 1304 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraphs (5), (6), (7), (8), (9), (10), (11), (12), (13), (14), (15), (16), and (17) as paragraphs (6), (7), (8), (10), (11), (12), (13), (14), (15), (16), (17), (18), and (19), respectively;\n**(B)**\nby inserting after paragraph (4) the following:\n(5) Controlled substance-related offense (A) In general The term controlled substance-related offense means a violation of the criminal law of the Indian tribe that has jurisdiction over the Indian country where the violation occurs that involves\u2014 (i) drug trafficking; (ii) unlawful drug possession; or (iii) unlawful possession of drug paraphernalia. (B) Associated definitions For purposes of this paragraph: (i) Controlled substance The term controlled substance means\u2014 (I) a controlled substance (as defined in section 102 of the Controlled Substances Act ( 21 U.S.C. 802 )); (II) a counterfeit substance (as defined in that section); and (III) a controlled substance analogue (as defined in that section). (ii) Drug paraphernalia The term drug paraphernalia has the meaning given the term in section 422(d) of the Controlled Substances Act ( 21 U.S.C. 863(d) ). (iii) Drug trafficking The term drug trafficking means\u2014 (I) the manufacture, cultivation, delivery, distribution, or dispensing of a controlled substance; (II) the possession of a controlled substance with the intent to manufacture, deliver, distribute, or dispense the controlled substance; and (III) the solicitation of, or the attempt or conspiracy to do, an act described in subclause (I) or (II). (iv) Unlawful drug possession The term unlawful drug possession means a violation of the criminal law of the Indian tribe that has jurisdiction over the Indian country where the violation occurs that involves the possession of a controlled substance. (v) Unlawful possession of drug paraphernalia The term unlawful possession of drug paraphernalia means a violation of the criminal law of the Indian tribe that has jurisdiction over the Indian country where the violation occurs that involves the possession of drug paraphernalia. ;\n**(C)**\nin paragraph (6) (as so redesignated)\u2014\n**(i)**\nin subparagraph (H), by striking and at the end;\n**(ii)**\nin subparagraph (I), by striking the period at the end and inserting a semicolon; and\n**(iii)**\nby adding at the end the following:\n(J) a controlled substance-related offense; and (K) a firearms offense. ; and\n**(D)**\nby inserting after paragraph (8) (as so redesignated) the following:\n(9) Firearms offense The term firearms offense means a violation of the criminal law of the Indian tribe that has jurisdiction over the Indian country where the violation occurs that involves the use or possession of a firearm\u2014 (A) in furtherance of a covered crime; or (B) by a person who has been convicted of domestic violence. ; and\n**(2)**\nin subsection (b)(4)(A), by striking or assault of Tribal justice personnel, and inserting , assault of Tribal justice personnel, a controlled substance-related offense, or a firearms offense, .\n#### 4. Bureau of Prisons Tribal Prisoner Program\nSection 234(c)(2)(B) of the Tribal Law and Order Act of 2010 ( 25 U.S.C. 1302a(2)(B) ) is amended by inserting or offenders convicted pursuant to the exercise of special Tribal criminal jurisdiction described in section 204 of Public Law 90\u2013284 (commonly known as the Indian Civil Rights Act of 1968 ) ( 25 U.S.C. 1304 ) after (comparable to the violent crimes described in section 1153(a) of title 18, United States Code) .",
      "versionDate": "2025-06-05",
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
        "actionDate": "2025-06-05",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3773",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PROTECT Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-01",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1574",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Tribal Access to Electronic Evidence Act",
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
        "name": "Native Americans",
        "updateDate": "2025-07-01T16:50:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-05",
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
          "measure-id": "id119s1967",
          "measure-number": "1967",
          "measure-type": "s",
          "orig-publish-date": "2025-06-05",
          "originChamber": "SENATE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1967v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2025-06-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protection for Reservation Occupants against Trafficking and Evasive Communications Today Act of 2025 or the PROTECT Act of 2025</strong></p><p>This bill expands special tribal criminal jurisdiction (STCJ) to include certain controlled substance-related offenses and firearms offenses. It also allows tribal courts to execute warrants for electronic material.</p><p>STCJ allows participating tribes to investigate, prosecute, convict, and sentence both Indian and non-Indian offenders who commit covered crimes in Indian country against Indian victims. Covered crimes currently include assault of tribal justice personnel, child violence, dating violence, domestic violence, obstruction of justice, sexual violence, sex trafficking, stalking, and a violation of a protection order.</p><p>The bill expands\u00a0STCJ to allow participating tribes to prosecute individuals for controlled substance-related offenses (i.e., drug trafficking, unlawful drug possession, or unlawful possession of drug paraphernalia) and firearms offenses (i.e., use or possession of a firearm in furtherance of a covered crime or by a person who has been convicted of domestic violence).</p><p>Additionally, the bill allows participating tribes to exercise\u00a0STCJ over a controlled substance-related offense or a firearms offense if neither the defendant nor the alleged victim is an Indian. (Currently, this\u00a0exception only applies in cases of obstruction of justice or assault of tribal justice personnel.)</p><p>The bill allows offenders convicted pursuant to STCJ to be incarcerated through the Bureau of Prisons Tribal Prisoner Program.</p><p>The bill gives tribal courts the same authority as state courts to compel service providers to disclose stored electronic communication information through court-issued warrants, court orders, or administrative subpoenas.</p>"
        },
        "title": "PROTECT Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1967.xml",
    "summary": {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protection for Reservation Occupants against Trafficking and Evasive Communications Today Act of 2025 or the PROTECT Act of 2025</strong></p><p>This bill expands special tribal criminal jurisdiction (STCJ) to include certain controlled substance-related offenses and firearms offenses. It also allows tribal courts to execute warrants for electronic material.</p><p>STCJ allows participating tribes to investigate, prosecute, convict, and sentence both Indian and non-Indian offenders who commit covered crimes in Indian country against Indian victims. Covered crimes currently include assault of tribal justice personnel, child violence, dating violence, domestic violence, obstruction of justice, sexual violence, sex trafficking, stalking, and a violation of a protection order.</p><p>The bill expands\u00a0STCJ to allow participating tribes to prosecute individuals for controlled substance-related offenses (i.e., drug trafficking, unlawful drug possession, or unlawful possession of drug paraphernalia) and firearms offenses (i.e., use or possession of a firearm in furtherance of a covered crime or by a person who has been convicted of domestic violence).</p><p>Additionally, the bill allows participating tribes to exercise\u00a0STCJ over a controlled substance-related offense or a firearms offense if neither the defendant nor the alleged victim is an Indian. (Currently, this\u00a0exception only applies in cases of obstruction of justice or assault of tribal justice personnel.)</p><p>The bill allows offenders convicted pursuant to STCJ to be incarcerated through the Bureau of Prisons Tribal Prisoner Program.</p><p>The bill gives tribal courts the same authority as state courts to compel service providers to disclose stored electronic communication information through court-issued warrants, court orders, or administrative subpoenas.</p>",
      "updateDate": "2026-03-13",
      "versionCode": "id119s1967"
    },
    "title": "PROTECT Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protection for Reservation Occupants against Trafficking and Evasive Communications Today Act of 2025 or the PROTECT Act of 2025</strong></p><p>This bill expands special tribal criminal jurisdiction (STCJ) to include certain controlled substance-related offenses and firearms offenses. It also allows tribal courts to execute warrants for electronic material.</p><p>STCJ allows participating tribes to investigate, prosecute, convict, and sentence both Indian and non-Indian offenders who commit covered crimes in Indian country against Indian victims. Covered crimes currently include assault of tribal justice personnel, child violence, dating violence, domestic violence, obstruction of justice, sexual violence, sex trafficking, stalking, and a violation of a protection order.</p><p>The bill expands\u00a0STCJ to allow participating tribes to prosecute individuals for controlled substance-related offenses (i.e., drug trafficking, unlawful drug possession, or unlawful possession of drug paraphernalia) and firearms offenses (i.e., use or possession of a firearm in furtherance of a covered crime or by a person who has been convicted of domestic violence).</p><p>Additionally, the bill allows participating tribes to exercise\u00a0STCJ over a controlled substance-related offense or a firearms offense if neither the defendant nor the alleged victim is an Indian. (Currently, this\u00a0exception only applies in cases of obstruction of justice or assault of tribal justice personnel.)</p><p>The bill allows offenders convicted pursuant to STCJ to be incarcerated through the Bureau of Prisons Tribal Prisoner Program.</p><p>The bill gives tribal courts the same authority as state courts to compel service providers to disclose stored electronic communication information through court-issued warrants, court orders, or administrative subpoenas.</p>",
      "updateDate": "2026-03-13",
      "versionCode": "id119s1967"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1967is.xml"
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
      "title": "PROTECT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T04:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PROTECT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T04:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protection for Reservation Occupants against Trafficking and Evasive Communications Today Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T04:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Stored Communications Act to include Tribal courts as courts of competent jurisdiction, to amend the Indian Civil Rights Act of 1968 to confer Tribal jurisdiction over controlled substances, related offenses, and firearms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T04:48:24Z"
    }
  ]
}
```
