# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1941?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1941
- Title: Preventing Deepfakes of Intimate Images Act
- Congress: 119
- Bill type: HR
- Bill number: 1941
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2026-04-06T16:07:38Z
- Update date including text: 2026-04-06T16:07:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1941",
    "number": "1941",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001206",
        "district": "25",
        "firstName": "Joseph",
        "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
        "lastName": "Morelle",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Preventing Deepfakes of Intimate Images Act",
    "type": "HR",
    "updateDate": "2026-04-06T16:07:38Z",
    "updateDateIncludingText": "2026-04-06T16:07:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
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
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:02:15Z",
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
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NJ"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MI"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NJ"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "IN"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "RI"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NJ"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "CT"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1941ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1941\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Morelle (for himself and Mr. Kean ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit the disclosure of intimate digital depictions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Deepfakes of Intimate Images Act .\n#### 2. Intimate digital depictions\nThe Violence Against Women Act Reauthorization Act of 2022 is amended by inserting after section 1309 the following:\n1309A. Disclosure of intimate digital depictions (a) Definitions In this section: (1) Consent The term consent has the meaning given such term in section 1309. (2) Depicted individual The term depicted individual means an individual who, as a result of digitization or by means of digital manipulation, appears in whole or in part in an intimate digital depiction and who is identifiable by virtue of the person\u2019s face, likeness, or other distinguishing characteristic, such as a unique birthmark or other recognizable feature, or from information displayed in connection with the digital depiction. (3) Digital depiction The term digital depiction means a realistic visual depiction, as that term is defined in section 2256(5) of title 18, United States Code, of an individual that has been created or altered using digital manipulation. (4) Disclose The term disclose has the meaning given such term in section 1309. (5) Intimate digital depiction The term intimate digital depiction means a digital depiction of an individual that has been created or altered using digital manipulation and that depicts\u2014 (A) the uncovered genitals, pubic area, anus, or postpubescent female nipple of an identifiable individual; (B) the display or transfer of bodily sexual fluids\u2014 (i) onto any part of the body of an identifiable individual; or (ii) from the body of an identifiable individual; or (C) an identifiable individual engaging in sexually explicit conduct. (6) Sexually explicit conduct The term sexually explicit conduct has the meaning given the term in subparagraphs (A) and (B) of section 2256(2) of title 18, United States Code. (b) Right of action (1) In general Except as provided in subsection (e), an individual who is the subject of an intimate digital depiction that is disclosed, in or affecting interstate or foreign commerce or using any means or facility of interstate or foreign commerce, without the consent of the individual, where such disclosure was made by a person who knows that, or recklessly disregards whether, the individual has not consented to such disclosure, may bring a civil action against that person in an appropriate district court of the United States for relief as set forth in subsection (d). (2) Rights on behalf of certain individuals In the case of an individual who have not attained 18 years of age or are incompetent, incapacitated, or deceased, the legal guardian of the individual or representative of the individual\u2019s estate, another family member, or any other person appointed as suitable by the court, may assume the individual\u2019s rights under this section, but in no event shall the defendant be named as such representative or guardian. (c) Consent For purposes of an action under subsection (b)\u2014 (1) an individual\u2019s consent to the creation of the intimate digital depiction shall not establish that the person consented to its disclosure; and (2) consent shall be deemed validly given only if\u2014 (A) it is set forth in an agreement written in plain language signed knowingly and voluntarily by the depicted individual; and (B) it includes a general description of the intimate digital depiction and, if applicable, the audiovisual work into which it will be incorporated. (d) Relief (1) In general (A) Damages In a civil action filed under this section, an individual may recover any of the following: (i) An amount equal to the monetary gain made by the defendant from the creation, development, or disclosure of the intimate digital depiction. (ii) Either of the following: (I) The actual damages sustained by the individual as a result of the intimate digital depiction, including damages for emotional distress. (II) Liquidated damages in the amount of $150,000. (iii) Punitive damages. (iv) The cost of the action, including reasonable attorney\u2019s fees and other litigation costs reasonably incurred. (B) Equitable relief In a civil action filed under this section, a court may, in addition to any other relief available at law, order equitable relief, including a temporary restraining order, a preliminary injunction, or a permanent injunction ordering the defendant to cease display or disclosure of the intimate digital depiction. (2) Preservation of anonymity In ordering relief under this subsection, the court may grant injunctive relief maintaining the confidentiality of a plaintiff using a pseudonym. (e) Exceptions An identifiable individual may not bring an action for relief under this section relating to\u2014 (1) a disclosure made in good faith\u2014 (A) to or by a law enforcement officer or agency in the course of reporting or investigating\u2014 (i) unlawful activity; or (ii) unsolicited or unwelcome conduct; or (B) as part of a legal proceeding; (2) a matter of legitimate public concern or public interest, except that it shall not be considered a matter of legitimate public interest or public concern solely because the depicted individual is a public figure; or (3) a disclosure reasonably intended to assist the identifiable individual. (f) In camera A court may authorize an in camera proceeding under this section. (g) Disclaimers It shall not be a defense to an action under this section that there is a disclaimer stating that the intimate digital depiction of the depicted individual was unauthorized or that the depicted individual did not participate in the creation or development of the material. (h) Limitations For purposes of this section, a provider of an interactive computer service shall not be held liable on account of\u2014 (1) any action voluntarily taken in good faith to restrict access to or availability of intimate digital depictions; or (2) any action taken to enable or make available to information content providers or other persons the technical means to restrict access to intimate digital depictions. .\n#### 3. Criminal action\n##### (a) In general\nChapter 110 of title 18, United States Code, is amended by inserting after section 2252C the following:\n2252D. Intimate digital depictions (a) Offense Whoever, in or affecting interstate or foreign commerce, discloses or threatens to disclose an intimate digital depiction\u2014 (1) with the intent to harass, annoy, threaten, alarm, or cause substantial harm to the finances or reputation of the depicted individual; or (2) with actual knowledge that, or reckless disregard for whether, such disclosure or threatened disclosure will cause physical, emotional, reputational, or economic harm to the depicted individual, shall be punished as provided under subsection (b). (b) Penalty Any person who commits an offense under subsection (a) shall be\u2014 (1) fined under this title, imprisoned for not more than 2 years, or both; or (2) fined under this title, imprisoned for not more than 10 years, or both, in the case of a violation in which the creation, reproduction, or distribution of the intimate digital depiction could be reasonably expected to\u2014 (A) affect the conduct of any administrative, legislative, or judicial proceeding of a Federal, State, local, or Tribal government agency, including the administration of an election or the conduct of foreign relations; or (B) facilitate violence. (c) Disclaimers It shall not be a defense to an action under this section that there is a disclaimer stating that the intimate digital depiction of the depicted individual was unauthorized or that the depicted individual did not participate in the creation or development of the material. (d) Limitations For purposes of this section, a provider of an interactive computer service shall not be held liable on account of\u2014 (1) any action voluntarily taken in good faith to restrict access to or availability of intimate digital depictions; or (2) any action taken to enable or make available to information content providers or other persons the technical means to restrict access to intimate digital depictions. (e) Definitions In this section: (1) Consent The term consent has the meaning given such term in section 1309 of the Violence Against Women Act Reauthorization Act of 2022. (2) Depicted individual The term depicted individual means an individual who, as a result of digitization or by means of digital manipulation, appears in whole or in part in an intimate digital depiction and who is identifiable by virtue of the person\u2019s face, likeness, or other distinguishing characteristic, such as a unique birthmark or other recognizable feature, or from information displayed in connection with the digital depiction. (3) Digital depiction The term digital depiction means a realistic visual depiction, as that term is defined in section 2256(5), of an individual that has been created or altered using digital manipulation. (4) Disclose The term disclose has the meaning given such term in section 1309 of the Violence Against Women Act Reauthorization Act of 2022. (5) Intimate digital depiction The term intimate digital depiction means a digital depiction of an individual that has been created or altered using digital manipulation and that depicts\u2014 (A) the uncovered genitals, pubic area, anus, or postpubescent female nipple of an identifiable individual; (B) the display or transfer of bodily sexual fluids\u2014 (i) onto any part of the body of an identifiable individual; or (ii) from the body of an identifiable individual; or (C) an identifiable individual engaging in sexually explicit conduct. (6) Sexually explicit conduct The term sexually explicit conduct has the meaning given the term in subparagraphs (A) and (B) of section 2256(2). .\n##### (b) Clerical amendment\nThe table of sections for chapter 110 of title 18, United States Code is amended by inserting after the item relating to section 2252C the following new item:\n2252D. Intimate digital depictions. .",
      "versionDate": "2025-03-06",
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
        "updateDate": "2025-03-25T14:39:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
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
          "measure-id": "id119hr1941",
          "measure-number": "1941",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1941v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Preventing Deepfakes of Intimate Images Act</b></p> <p>This bill makes it a crime to intentionally disclose (or threaten to disclose) a digital depiction that has been altered using digital manipulation of an individual engaging in sexually explicit conduct. </p>"
        },
        "title": "Preventing Deepfakes of Intimate Images Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1941.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Preventing Deepfakes of Intimate Images Act</b></p> <p>This bill makes it a crime to intentionally disclose (or threaten to disclose) a digital depiction that has been altered using digital manipulation of an individual engaging in sexually explicit conduct. </p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr1941"
    },
    "title": "Preventing Deepfakes of Intimate Images Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Preventing Deepfakes of Intimate Images Act</b></p> <p>This bill makes it a crime to intentionally disclose (or threaten to disclose) a digital depiction that has been altered using digital manipulation of an individual engaging in sexually explicit conduct. </p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr1941"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1941ih.xml"
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
      "title": "Preventing Deepfakes of Intimate Images Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Deepfakes of Intimate Images Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the disclosure of intimate digital depictions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:18:27Z"
    }
  ]
}
```
