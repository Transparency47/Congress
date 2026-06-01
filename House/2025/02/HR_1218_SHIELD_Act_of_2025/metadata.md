# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1218?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1218
- Title: SHIELD Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1218
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2025-12-05T21:42:26Z
- Update date including text: 2025-12-05T21:42:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1218",
    "number": "1218",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "SHIELD Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:42:26Z",
    "updateDateIncludingText": "2025-12-05T21:42:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
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
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:04:50Z",
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
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "SC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "CA"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "VI"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "GA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "GA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "VA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "NY"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1218ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1218\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Mr. Van Drew (for himself, Ms. Dean of Pennsylvania , Ms. Mace , Mr. Fitzpatrick , Mr. Moran , Ms. Salazar , Mr. Nehls , Mr. Kiley of California , Ms. Plaskett , Mrs. McBath , Mr. Johnson of Georgia , and Ms. Scanlon ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide that it is unlawful to knowingly distribute private intimate visual depictions with reckless disregard for the individual\u2019s lack of consent to the distribution, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Harmful Image Exploitation and Limiting Distribution Act of 2025 or the SHIELD Act of 2025 .\n#### 2. Certain activities relating to intimate visual depictions\n##### (a) In general\nChapter 88 of title 18, United States Code, is amended by adding at the end the following:\n1802. Certain activities relating to intimate visual depictions (a) Definitions In this section: (1) Communications service The term communications service means\u2014 (A) a service provided by a person that is a common carrier, as that term is defined in section 3 of the Communications Act of 1934 ( 47 U.S.C. 153 ), insofar as the person is acting as a common carrier; (B) an electronic communication service, as that term is defined in section 2510; (C) an information service, as that term is defined in section 3 of the Communications Act of 1934 ( 47 U.S.C. 153 ); and (D) an interactive computer service, as that term is defined in section 230(f) of the Communications Act of 1934 ( 47 U.S.C. 230(f) ). (2) Information content provider The term information content provider has the meaning given that term in section 230(f) of the Communications Act of 1934 ( 47 U.S.C. 230(f) ). (3) Intimate visual depiction The term intimate visual depiction means any visual depiction (as that term is defined in section 2256(5)) of an individual\u2014 (A) who has attained 18 years of age at the time the intimate visual depiction is created; (B) who is recognizable to a third party from the intimate image itself or information or text displayed in connection with the intimate image itself or information or text displayed in connection with the intimate image; and (C) (i) who is depicted engaging in sexually explicit conduct; or (ii) whose genitals, anus, pubic area, or female nipple are unclothed and visible. (4) Minor The term minor has the meaning given that term in section 2256. (5) Sexually explicit conduct The term sexually explicit conduct has the meaning given that term in section 2256(2)(A). (6) Visual depiction of a nude minor The term visual depiction of a nude minor means any visual depiction (as that term is defined in section 2256(5)) of an individual who is recognizable by an individual other than the depicted individual from the intimate image itself or information or text displayed in connection with the intimate image who was under 18 years of age at the time the visual depiction was created in which the actual anus, genitals, or pubic area, or post-pubescent female nipple, of the minor are unclothed, visible, and displayed in a manner that does not constitute sexually explicit conduct. (b) Offenses (1) In general Except as provided in subsection (d), it shall be unlawful to knowingly mail, or to knowingly distribute using any means or facility of interstate or foreign commerce or affecting interstate or foreign commerce, an intimate visual depiction of an individual\u2014 (A) that was obtained or created under circumstances in which the actor knew or reasonably should have known the individual depicted had a reasonable expectation of privacy; (B) where what is depicted was not voluntarily exposed by the individual in a public or commercial setting; (C) where what is depicted is not a matter of public concern; and (D) if the distribution\u2014 (i) is intended to cause harm; or (ii) causes harm, including psychological, financial, or reputational harm, to the individual depicted. For purposes of this paragraph, the fact that the subject of the depiction consented to the creation of the depiction shall not establish that that person consented to its distribution. (2) Involving minors Except as provided in subsection (d), it shall be unlawful to knowingly mail, or to knowingly distribute using any means or facility of interstate or foreign commerce or affecting interstate or foreign commerce, a visual depiction of a nude minor with intent to abuse, humiliate, harass, or degrade the minor, or to arouse or gratify the sexual desire of any person. (c) Penalty (1) In general (A) Visual depiction of a nude minor Any person who violates subsection (b)(2) shall be fined under this title, imprisoned not more than 3 years, or both. (B) Intimate visual depiction Any person who violates subsection (b)(1) shall be fined under this title, imprisoned for not more than 2 years, or both. (2) Forfeiture (A) In general The court, in imposing a sentence on any person convicted of a violation involving intimate visual depictions or visual depictions of a nude minor under this section, or convicted of a conspiracy of a violation involving intimate visual depictions or visual depictions of a nude minor under this section, shall order, in addition to any other sentence imposed and irrespective of any provision of State law, that such person forfeit to the United States\u2014 (i) any material distributed in violation of this section; (ii) such person\u2019s interest in property, real or personal, constituting or derived from any gross proceeds of such violation, or any property traceable to such property, obtained or retained directly or indirectly as a result of such violation; and (iii) any personal property of the person used, or intended to be used, in any manner or part, to commit or to facilitate the commission of such violation. (B) Procedures Section 413 of the Controlled Substances Act ( 21 U.S.C. 853 ), with the exception of subsections (a) and (d), applies to the criminal forfeiture of property pursuant to subparagraph (A). (3) Restitution Restitution shall be available as provided in section 2264 of this title. (d) Exceptions (1) Law enforcement, lawful reporting, and other legal proceedings This section\u2014 (A) does not prohibit any lawfully authorized investigative, protective, or intelligence activity of a law enforcement agency of the United States, a State, or a political subdivision of a State, or of an intelligence agency of the United States; and (B) shall not apply to distributions that are made reasonably and in good faith\u2014 (i) to report unlawful or unsolicited activity or in pursuance of a legal or professional or other lawful obligation; (ii) to seek support or help with respect to the receipt of an unsolicited intimate visual depiction; (iii) relating to an individual who possesses or distributes a visual depiction of himself or herself engaged in nudity or sexually explicit conduct; (iv) to assist the depicted individual; (v) for legitimate medical, scientific, or educational purposes; or (vi) as part of a document production or filing associated with a legal proceeding. (2) Service providers This section shall not apply to any provider of a communications service with regard to content provided by another information content provider unless the provider of the communications service intentionally solicits, or knowingly and predominantly distributes, such content. (e) Threats Any person who intentionally threatens to commit an offense under subsection (b) for the purpose of intimidation, coercion, extortion, or to create mental distress shall be punished as provided in subsection (c). (f) Extraterritoriality There is extraterritorial Federal jurisdiction over an offense under this section if the defendant or the depicted individual is a citizen or permanent resident of the United States. (g) Rule of construction Nothing in this section shall be construed to limit the application of any other relevant law, including section 2252 of this title. .\n##### (b) Clerical amendment\nThe table of sections for chapter 88 of title 18, United States Code, is amended by inserting after the item relating to section 1801 the following:\n1802. Certain activities relating to intimate visual depictions. .\n##### (c) Conforming amendment\nSection 2264(a) of title 18, United States Code, is amended by inserting , or under section 1802 of this title before the period.",
      "versionDate": "2025-02-11",
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
        "actionDate": "2025-02-11",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "516",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SHIELD Act of 2023",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-05-02T14:54:00Z"
          },
          {
            "name": "Crimes against children",
            "updateDate": "2025-05-02T14:54:00Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-05-02T14:54:00Z"
          },
          {
            "name": "Domestic violence and child abuse",
            "updateDate": "2025-05-02T14:54:00Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-05-02T14:54:00Z"
          },
          {
            "name": "Pornography",
            "updateDate": "2025-05-02T14:54:00Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-05-02T14:54:00Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-05-02T14:54:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-13T13:50:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119hr1218",
          "measure-number": "1218",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-11",
          "originChamber": "HOUSE",
          "update-date": "2025-08-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1218v00",
            "update-date": "2025-08-26"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stopping Harmful Image Exploitation and Limiting Distribution Act of 2025 or the SHIELD Act of 2025</strong></p><p>This bill establishes new federal criminal offenses related to the distribution of sexual exploitative content.\u00a0</p><p>First, the bill makes it a crime to knowingly mail or distribute (or intentionally threaten to mail or distribute) an intimate visual depiction of a\u00a0recognizable adult engaged in sexual conduct.\u00a0To constitute a crime, certain elements must be met, including that the distribution must be nonconsensual; the depiction is not a matter of public concern; and the distribution must be intended to cause harm or cause harm.\u00a0A violator is subject to a fine, a prison term of up to two years, or both; mandatory restitution; and the forfeiture of material involved in the offense, property constituting or derived from the proceeds from the offense, and property used to commit or facilitate the offense.</p><p>Second, the bill makes it a crime\u00a0to knowingly mail or distribute (or intentionally threaten to mail or distribute) a visual depiction of a nude minor with intent to abuse, humiliate, harass, or degrade the minor, or to arouse or gratify the sexual desire of any person. A violator is subject to a fine, a prison term of up to three years, or both; mandatory restitution; and the forfeiture of material involved in the offense, property constituting or derived from the proceeds from the offense, and property used to commit or facilitate the offense.</p>"
        },
        "title": "SHIELD Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1218.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stopping Harmful Image Exploitation and Limiting Distribution Act of 2025 or the SHIELD Act of 2025</strong></p><p>This bill establishes new federal criminal offenses related to the distribution of sexual exploitative content.\u00a0</p><p>First, the bill makes it a crime to knowingly mail or distribute (or intentionally threaten to mail or distribute) an intimate visual depiction of a\u00a0recognizable adult engaged in sexual conduct.\u00a0To constitute a crime, certain elements must be met, including that the distribution must be nonconsensual; the depiction is not a matter of public concern; and the distribution must be intended to cause harm or cause harm.\u00a0A violator is subject to a fine, a prison term of up to two years, or both; mandatory restitution; and the forfeiture of material involved in the offense, property constituting or derived from the proceeds from the offense, and property used to commit or facilitate the offense.</p><p>Second, the bill makes it a crime\u00a0to knowingly mail or distribute (or intentionally threaten to mail or distribute) a visual depiction of a nude minor with intent to abuse, humiliate, harass, or degrade the minor, or to arouse or gratify the sexual desire of any person. A violator is subject to a fine, a prison term of up to three years, or both; mandatory restitution; and the forfeiture of material involved in the offense, property constituting or derived from the proceeds from the offense, and property used to commit or facilitate the offense.</p>",
      "updateDate": "2025-08-26",
      "versionCode": "id119hr1218"
    },
    "title": "SHIELD Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stopping Harmful Image Exploitation and Limiting Distribution Act of 2025 or the SHIELD Act of 2025</strong></p><p>This bill establishes new federal criminal offenses related to the distribution of sexual exploitative content.\u00a0</p><p>First, the bill makes it a crime to knowingly mail or distribute (or intentionally threaten to mail or distribute) an intimate visual depiction of a\u00a0recognizable adult engaged in sexual conduct.\u00a0To constitute a crime, certain elements must be met, including that the distribution must be nonconsensual; the depiction is not a matter of public concern; and the distribution must be intended to cause harm or cause harm.\u00a0A violator is subject to a fine, a prison term of up to two years, or both; mandatory restitution; and the forfeiture of material involved in the offense, property constituting or derived from the proceeds from the offense, and property used to commit or facilitate the offense.</p><p>Second, the bill makes it a crime\u00a0to knowingly mail or distribute (or intentionally threaten to mail or distribute) a visual depiction of a nude minor with intent to abuse, humiliate, harass, or degrade the minor, or to arouse or gratify the sexual desire of any person. A violator is subject to a fine, a prison term of up to three years, or both; mandatory restitution; and the forfeiture of material involved in the offense, property constituting or derived from the proceeds from the offense, and property used to commit or facilitate the offense.</p>",
      "updateDate": "2025-08-26",
      "versionCode": "id119hr1218"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1218ih.xml"
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
      "title": "SHIELD Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T12:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SHIELD Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T12:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Harmful Image Exploitation and Limiting Distribution Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T12:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that it is unlawful to knowingly distribute private intimate visual depictions with reckless disregard for the individual's lack of consent to the distribution, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T12:48:44Z"
    }
  ]
}
```
