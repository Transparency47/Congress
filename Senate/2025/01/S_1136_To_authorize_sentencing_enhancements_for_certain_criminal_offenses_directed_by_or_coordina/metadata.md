# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1136?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1136
- Title: DETERRENCE Act
- Congress: 119
- Bill type: S
- Bill number: 1136
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2026-04-09T20:50:23Z
- Update date including text: 2026-04-09T20:50:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-06-10 - Committee: Committee on Homeland Security and Governmental Affairs Subcommittee on Border Management, Federal Workforce, and Regulatory Affairs. Hearings held.
- 2025-06-10 - Floor: Passed Senate without amendment by Unanimous Consent. (text: CR S3322-3323)
- 2025-06-10 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-06-10 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-06-10 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent. (consideration: CR S3322-3323)
- 2025-06-11 - Floor: Message on Senate action sent to the House.
- 2025-06-11 13:31:38 - Floor: Received in the House.
- 2025-06-11 13:35:46 - Floor: Held at the desk.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-06-10 - Committee: Committee on Homeland Security and Governmental Affairs Subcommittee on Border Management, Federal Workforce, and Regulatory Affairs. Hearings held.
- 2025-06-10 - Floor: Passed Senate without amendment by Unanimous Consent. (text: CR S3322-3323)
- 2025-06-10 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-06-10 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-06-10 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent. (consideration: CR S3322-3323)
- 2025-06-11 - Floor: Message on Senate action sent to the House.
- 2025-06-11 13:31:38 - Floor: Received in the House.
- 2025-06-11 13:35:46 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1136",
    "number": "1136",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
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
    "title": "DETERRENCE Act",
    "type": "S",
    "updateDate": "2026-04-09T20:50:23Z",
    "updateDateIncludingText": "2026-04-09T20:50:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-06-11",
      "actionTime": "13:35:46",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-06-11",
      "actionTime": "13:31:38",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (text: CR S3322-3323)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent. (consideration: CR S3322-3323)",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Border Management, Federal Workforce, and Regulatory Affairs Subcommittee",
          "systemCode": "ssga22"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs Subcommittee on Border Management, Federal Workforce, and Regulatory Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-26",
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
            "date": "2025-06-10T22:50:00Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-03-26T15:31:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
      "type": "Standing"
    },
    {
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-10T16:01:32Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Border Management, Federal Workforce, and Regulatory Affairs Subcommittee",
          "systemCode": "ssga22"
        }
      },
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "IA"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "IN"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1136is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1136\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Ms. Hassan (for herself, Ms. Ernst , Mr. Banks , and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo authorize sentencing enhancements for certain criminal offenses directed by or coordinated with foreign governments.\n#### 1. Short title\nThis Act may be cited as the Deterring External Threats and Ensuring Robust Responses to Egregious and Nefarious Criminal Endeavors Act or the DETERRENCE Act .\n#### 2. Kidnapping\nSection 1201 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (h) as subsection (i);\n**(2)**\nby inserting after subsection (g) the following:\n(h) Sentence enhancements for offenses directed by or coordinated with foreign governments (1) In general The sentence of a person convicted of an offense under subsection (a) may be increased by up to 10 years if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. (2) Conspiracy The sentence of a person convicted of conspiring to commit a violation of subsection (a) as part of a conspiracy under the elements specified in subsection (c) may be increased by up to 10 years if\u2014 (A) 1 or more of the persons involved in such conspiracy were knowingly acting in coordination with a foreign government or an agent of a foreign government; and (B) the person convicted of conspiring to commit a violation of subsection (a) knew that 1 or more of the persons involved in such conspiracy were knowingly acting in coordination with a foreign government or an agent of a foreign government. (3) Attempt The sentence of a person convicted of an attempt to violate subsection (a) may be increased by up to 5 years if such attempt was knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. ; and\n**(3)**\nin subsection (i), as so designated, by inserting Definition .\u2014 before As used in this section .\n#### 3. Use of interstate commerce facilities in the commission of murder-for-hire\n##### (a) In general\nSection 1958 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (b) as subsection (c);\n**(2)**\nby inserting after subsection (a) the following:\n(b) Sentence enhancements for offenses directed by or coordinated with foreign governments The sentence of a person convicted of an offense under subsection (a)\u2014 (1) may be increased by up to 5 years, if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government; and (2) may be increased by up to 10 years\u2014 (A) if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government; and (B) personal injury results. ; and\n**(3)**\nin subsection (c), as so redesignated, by inserting Definitions .\u2014 before As used in this section .\n##### (b) Technical and conforming amendments\n**(1)**\nSection 2332b(g)(2) of title 18, United States Code, is amended by striking section 1958(b)(2) and inserting section 1958 .\n**(2)**\nSection 1010A(d) of the Controlled Substances Import and Export Act ( 21 U.S.C. 960a(d) ) is amended by striking section 1958(b)(1) and inserting section 1958 .\n#### 4. Influencing, impeding, or retaliating against a federal official by threatening or injuring a family member\nSection 115(b) of title 18, United States Code, is amended by adding at the end the following:\n(5) The sentence of a person convicted of an offense under subsection (a), if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government\u2014 (A) may be increased by up to 5 years if the offense committed was an assault involving physical contact with the victim of that assault or the intent to commit another felony; (B) may be increased by up to 10 years if\u2014 (i) the offense committed was an assault resulting in bodily injury (including serious bodily injury (as that term is defined in section 1365 of this title)); (ii) the offense involved any conduct that, if the conduct occurred in the special maritime and territorial jurisdiction of the United States, would violate section 2241 or 2242 of this title; or (iii) a dangerous weapon was used during and in relation to the offense; and (C) may be increased by up to 10 years if the offense committed was a murder, attempted murder, or conspiracy to murder. .\n#### 5. Stalking\nSection 2261A of title 18, United States Code, is amended\u2014\n**(1)**\nby striking Whoever\u2014 and inserting (a) In general .\u2014Except as provided in subsection (b), whoever\u2014 ; and\n**(2)**\nby adding at the end the following:\n(b) Enhanced penalties for offenses involving foreign governments The sentence of a person convicted of an offense under paragraph (1) or (2) of subsection (a), if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government\u2014 (1) may be increased by up to 5 years if\u2014 (A) serious bodily injury (including permanent disfigurement or life threatening bodily injury) to the victim results; (B) the offender uses a dangerous weapon during the offense; or (C) the victim of the offense is under the age of 18 years; (2) may be increased by up to 10 years if death of the victim results; and (3) may be increased by up to 30 months in any other case. .\n#### 6. Protection of officers and employees of the United States\nSection 1114 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (b) as subsection (c); and\n**(2)**\nby inserting after subsection (a) the following:\n(b) Sentence enhancements for offenses directed by or coordinated with foreign governments The sentence of a person convicted of an offense under subsection (a) may be increased by up to 10 years if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. .\n#### 7. Presidential and Presidential staff assassination, kidnapping, and assault\nSection 1751 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (f) through (k) as subsections (g) through (i), respectively; and\n**(2)**\nby inserting after subsection (e) the following:\n(f) (1) The sentence of a person convicted of an offense under subsection (a), (b), or (c) may be increased by up to 10 years if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. (2) The sentence of a person convicted of conspiring to kill or kidnap any individual designated in subsection (a) as part of a conspiracy under the elements specified in subsection (d) may be increased by up to 10 years if\u2014 (A) 1 or more of the persons involved in such conspiracy were knowingly acting in coordination with a foreign government or an agent of a foreign government; and (B) the person convicted of conspiring to kill or kidnap an individual designated in subsection (a) knew that 1 or more of the persons involved in such conspiracy were knowingly acting in coordination with a foreign government or an agent of a foreign government. (3) The sentence of a person convicted of an offense under subsection (e) may be increased by up to 10 years if\u2014 (A) the victim was any person designated in subsection (a)(1); and (B) such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. (4) The sentence of a person convicted of an offense under subsection (e) may be increased by up to 10 years if\u2014 (A) the victim was any person designated in subsection (a)(2); and (B) such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. (5) The sentence of a person convicted of an offense under subsection (e) may be increased by up to 10 years if\u2014 (A) (i) the offense involved the use of a dangerous weapon; or (ii) personal injury resulted; and (B) such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. .",
      "versionDate": "2025-03-26",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1136es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1136\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo authorize sentencing enhancements for certain criminal offenses directed by or coordinated with foreign governments.\n#### 1. Short title\nThis Act may be cited as the Deterring External Threats and Ensuring Robust Responses to Egregious and Nefarious Criminal Endeavors Act or the DETERRENCE Act .\n#### 2. Kidnapping\nSection 1201 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (h) as subsection (i);\n**(2)**\nby inserting after subsection (g) the following:\n(h) Sentence enhancements for offenses directed by or coordinated with foreign governments (1) In general The sentence of a person convicted of an offense under subsection (a) may be increased by up to 10 years if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. (2) Conspiracy The sentence of a person convicted of conspiring to commit a violation of subsection (a) as part of a conspiracy under the elements specified in subsection (c) may be increased by up to 10 years if\u2014 (A) 1 or more of the persons involved in such conspiracy were knowingly acting in coordination with a foreign government or an agent of a foreign government; and (B) the person convicted of conspiring to commit a violation of subsection (a) knew that 1 or more of the persons involved in such conspiracy were knowingly acting in coordination with a foreign government or an agent of a foreign government. (3) Attempt The sentence of a person convicted of an attempt to violate subsection (a) may be increased by up to 5 years if such attempt was knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. ; and\n**(3)**\nin subsection (i), as so designated, by inserting Definition .\u2014 before As used in this section .\n#### 3. Use of interstate commerce facilities in the commission of murder-for-hire\n##### (a) In general\nSection 1958 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (b) as subsection (c);\n**(2)**\nby inserting after subsection (a) the following:\n(b) Sentence enhancements for offenses directed by or coordinated with foreign governments The sentence of a person convicted of an offense under subsection (a)\u2014 (1) may be increased by up to 5 years, if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government; and (2) may be increased by up to 10 years\u2014 (A) if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government; and (B) personal injury results. ; and\n**(3)**\nin subsection (c), as so redesignated, by inserting Definitions .\u2014 before As used in this section .\n##### (b) Technical and conforming amendments\n**(1)**\nSection 2332b(g)(2) of title 18, United States Code, is amended by striking section 1958(b)(2) and inserting section 1958 .\n**(2)**\nSection 1010A(d) of the Controlled Substances Import and Export Act ( 21 U.S.C. 960a(d) ) is amended by striking section 1958(b)(1) and inserting section 1958 .\n#### 4. Influencing, impeding, or retaliating against a federal official by threatening or injuring a family member\nSection 115(b) of title 18, United States Code, is amended by adding at the end the following:\n(5) The sentence of a person convicted of an offense under subsection (a), if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government\u2014 (A) may be increased by up to 5 years if the offense committed was an assault involving physical contact with the victim of that assault or the intent to commit another felony; (B) may be increased by up to 10 years if\u2014 (i) the offense committed was an assault resulting in bodily injury (including serious bodily injury (as that term is defined in section 1365 of this title)); (ii) the offense involved any conduct that, if the conduct occurred in the special maritime and territorial jurisdiction of the United States, would violate section 2241 or 2242 of this title; or (iii) a dangerous weapon was used during and in relation to the offense; and (C) may be increased by up to 10 years if the offense committed was a murder, attempted murder, or conspiracy to murder. .\n#### 5. Stalking\nSection 2261A of title 18, United States Code, is amended\u2014\n**(1)**\nby striking Whoever\u2014 and inserting (a) In general .\u2014Except as provided in subsection (b), whoever\u2014 ; and\n**(2)**\nby adding at the end the following:\n(b) Enhanced penalties for offenses involving foreign governments The sentence of a person convicted of an offense under paragraph (1) or (2) of subsection (a), if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government\u2014 (1) may be increased by up to 5 years if\u2014 (A) serious bodily injury (including permanent disfigurement or life threatening bodily injury) to the victim results; (B) the offender uses a dangerous weapon during the offense; or (C) the victim of the offense is under the age of 18 years; (2) may be increased by up to 10 years if death of the victim results; and (3) may be increased by up to 30 months in any other case. .\n#### 6. Protection of officers and employees of the United States\nSection 1114 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (b) as subsection (c); and\n**(2)**\nby inserting after subsection (a) the following:\n(b) Sentence enhancements for offenses directed by or coordinated with foreign governments The sentence of a person convicted of an offense under subsection (a) may be increased by up to 10 years if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. .\n#### 7. Presidential and Presidential staff assassination, kidnapping, and assault\nSection 1751 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (f) through (k) as subsections (g) through (i), respectively; and\n**(2)**\nby inserting after subsection (e) the following:\n(f) (1) The sentence of a person convicted of an offense under subsection (a), (b), or (c) may be increased by up to 10 years if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. (2) The sentence of a person convicted of conspiring to kill or kidnap any individual designated in subsection (a) as part of a conspiracy under the elements specified in subsection (d) may be increased by up to 10 years if\u2014 (A) 1 or more of the persons involved in such conspiracy were knowingly acting in coordination with a foreign government or an agent of a foreign government; and (B) the person convicted of conspiring to kill or kidnap an individual designated in subsection (a) knew that 1 or more of the persons involved in such conspiracy were knowingly acting in coordination with a foreign government or an agent of a foreign government. (3) The sentence of a person convicted of an offense under subsection (e) may be increased by up to 10 years if\u2014 (A) the victim was any person designated in subsection (a)(1); and (B) such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. (4) The sentence of a person convicted of an offense under subsection (e) may be increased by up to 10 years if\u2014 (A) the victim was any person designated in subsection (a)(2); and (B) such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. (5) The sentence of a person convicted of an offense under subsection (e) may be increased by up to 10 years if\u2014 (A) (i) the offense involved the use of a dangerous weapon; or (ii) personal injury resulted; and (B) such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-03-26",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2394",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DETERRENCE Act",
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
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-06-23T19:20:26Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-06-23T19:26:01Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2025-06-23T19:18:18Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-06-23T19:20:44Z"
          },
          {
            "name": "Presidential administrations",
            "updateDate": "2025-06-23T19:25:42Z"
          },
          {
            "name": "Subversive activities",
            "updateDate": "2025-06-23T19:19:22Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2025-06-23T19:28:35Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-06-23T19:19:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-08T17:56:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-10",
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
          "measure-id": "id119s1136",
          "measure-number": "1136",
          "measure-type": "s",
          "orig-publish-date": "2025-06-10",
          "originChamber": "SENATE",
          "update-date": "2026-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1136v55",
            "update-date": "2026-04-09"
          },
          "action-date": "2025-06-10",
          "action-desc": "Passed Senate",
          "summary-text": "<p><strong>Deterring External Threats and Ensuring Robust Responses to Egregious and Nefarious Criminal Endeavors Act or the DETERRENCE Act</strong></p><p>This bill establishes sentencing enhancements for various federal criminal offenses if the offenses are directed by or coordinated with a foreign government.</p>"
        },
        "title": "DETERRENCE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1136.xml",
    "summary": {
      "actionDate": "2025-06-10",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Deterring External Threats and Ensuring Robust Responses to Egregious and Nefarious Criminal Endeavors Act or the DETERRENCE Act</strong></p><p>This bill establishes sentencing enhancements for various federal criminal offenses if the offenses are directed by or coordinated with a foreign government.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119s1136"
    },
    "title": "DETERRENCE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-10",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Deterring External Threats and Ensuring Robust Responses to Egregious and Nefarious Criminal Endeavors Act or the DETERRENCE Act</strong></p><p>This bill establishes sentencing enhancements for various federal criminal offenses if the offenses are directed by or coordinated with a foreign government.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119s1136"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1136is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1136es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "DETERRENCE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T11:03:16Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "DETERRENCE Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-06-11T03:53:17Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Deterring External Threats and Ensuring Robust Responses to Egregious and Nefarious Criminal Endeavors Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-06-11T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DETERRENCE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Deterring External Threats and Ensuring Robust Responses to Egregious and Nefarious Criminal Endeavors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize sentencing enhancements for certain criminal offenses directed by or coordinated with foreign governments.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:24Z"
    }
  ]
}
```
