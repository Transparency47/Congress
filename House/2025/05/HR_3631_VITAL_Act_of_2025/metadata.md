# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3631?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3631
- Title: VITAL Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3631
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2025-06-03T13:07:28Z
- Update date including text: 2025-06-03T13:07:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3631",
    "number": "3631",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000590",
        "district": "7",
        "firstName": "Mark",
        "fullName": "Rep. Green, Mark E. [R-TN-7]",
        "lastName": "Green",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "VITAL Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-03T13:07:28Z",
    "updateDateIncludingText": "2025-06-03T13:07:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-29T15:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3631ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3631\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Green of Tennessee introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo criminalize fraudulent statements made with respect to clinical vaccine trials.\n#### 1. Short title\nThis Act may be cited as the Vaccines in Trial and Liability Act of 2025 or the VITAL Act of 2025 .\n#### 2. Medical research company or sponsor\n##### (a) In general\nChapter 47 of title 18, United States Code, is amended by adding at the end the following:\n1041. Clinical vaccine trial fraud Whoever, being a medical research company or sponsor, makes a fraudulent statement to, or conceals from, any department or agency of the United States, any material data collected from a clinical vaccine trial, shall be fined under this title, imprisoned not more than 5 years, or both. .\n##### (b) Clerical amendment\nThe table of sections for chapter 47 of title 18, United States Code, is amended by adding at the end the following:\n1041. Clinical vaccine trial fraud. .\n#### 3. Scope of authorization\nSection 564(c) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360bbb\u20133(c) ) is amended\u2014\n**(1)**\nin paragraph (4), by striking and ;\n**(2)**\nby redesignating paragraph (5) as paragraph (6); and\n**(3)**\nby inserting after paragraph (4) the following:\n(5) the authorization is based on a certification by a medical research company or sponsor that no fraudulent material statements were made, and no material information was concealed, with respect to the circumstances described under subsection (b)(1) or the criteria under this subsection; and .\n#### 4. Revision and revocation\nSection 564(g)(2) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360bbb\u20133(g)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking or at the end;\n**(2)**\nby redesignating subparagraph (C) as subparagraph (D); and\n**(3)**\nby inserting after subparagraph (B) the following:\n(C) the Secretary determines that fraudulent material statements were made, or material information was concealed, with respect to the circumstances described under subsection (b)(1) or the criteria under subsection (c); or .\n#### 5. Exception to limitation on liability\nSection 2(b)(1) of the Trickett Wendler, Frank Mongiello, Jordan McLinn, and Matthew Bellina Right to Try Act of 2017 (21 U.S.C. 360bbb\u20130a note) is amended\u2014\n**(1)**\nin subparagraph (A), by inserting , unless a fraudulent material statement was made, or material information was concealed, with respect to data collected from a clinical trial of the investigational drug before the semicolon; and\n**(2)**\nin subparagraph (B), by inserting , including a fraudulent material statement made, or material information concealed, with respect to data collected from a clinical trial of the investigational drug before the period.\n#### 6. Exception to targeted liability protections for pandemic and epidemic products\nSection 319F\u20133 of the Public Health Service Act ( 42 U.S.C. 247d\u20136d ) is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(A)\u2014\n**(i)**\nby redesignating clauses (i), (ii), and (iii) as subclauses (I), (II), and (III), respectively;\n**(ii)**\nby moving subclauses (I), (II), and (III), as redesignated, 2 ems to the right;\n**(iii)**\nby striking the period at the end of subclause (III) and inserting ; and , as redesignated;\n**(iv)**\nby striking subsection (d), denote and inserting the following:\nsubsection (d)\u2014 (i) denote ; and\n**(v)**\nby adding at the end the following:\n(ii) includes\u2014 (I) making a fraudulent material statement with respect to data collected from a clinical trial; or (II) concealing material information with respect to data collected from a clinical trial. ; and\n**(B)**\nin paragraph (5)(A)\u2014\n**(i)**\nin the matter preceding clause (i), by striking subsection (d) if\u2014 and inserting subsection (d)\u2014 ;\n**(ii)**\nin clause (i)\u2014\n**(I)**\nby inserting if before neither ; and\n**(II)**\nby striking or at the end;\n**(iii)**\nin clause (ii)\u2014\n**(I)**\nby inserting if before such an enforcement ; and\n**(II)**\nby striking the period at the end and inserting ; and ; and\n**(iv)**\nby adding at the end the following:\n(iii) unless the Secretary determines, after notice and opportunity for a hearing, that a fraudulent material statement was made, or material information was concealed, by a covered person with respect to data collected from a clinical trial of a covered countermeasure. ; and\n**(2)**\nin subsection (e)\u2014\n**(A)**\nby striking paragraph (7); and\n**(B)**\nby adding at the end the following:\n(11) Award of damages Notwithstanding any other provision of law, the amount of an award of damages made to a plaintiff may not be reduced because of any other award for damages the plaintiff may receive as a result of such claim. .\n#### 7. National Vaccine Injury Compensation Program\nSection 2122 of the Public Health Service Act ( 42 U.S.C. 300aa\u201322 ) is amended by adding at the end the following:\n(f) Liability (1) Fraudulent material statement No civil action against a vaccine manufacturer or vaccine sponsor shall be barred under this part if the Secretary determines, after notice and opportunity for a hearing, that a fraudulent material statement was made, or material information was concealed, by a vaccine manufacturer with respect to data collected from a clinical trial of a vaccine. (2) Award of damages (A) In general Notwithstanding any other provision of law, an plaintiff bringing a claim pursuant to paragraph (1) may\u2014 (i) seek compensation under the program established under this part; and (ii) concurrently bring an action with respect to such claim in any appropriate United States district court. (B) Award of damages Notwithstanding any other provision of law, the amount of an award of damages made to a plaintiff for a claim pursuant to paragraph (1) may not be reduced on the basis of any other damages the plaintiff may receive as a result of such claim. (3) Applicability with respect to COVID\u201319 vaccine Notwithstanding any other provision of law, a civil action against a vaccine manufacturer pursuant to paragraph (1) with respect to a vaccine related to COVID\u201319 may be made at any time. (4) COVID\u201319 definition In this section, the term COVID\u201319 means the coronavirus disease caused by the severe acute respiratory syndrome coronavirus 2 or the SARS\u2013CoV\u20132. This term also relates to any and all variations of that virus of which there is no termination date for this term.\n#### 8. Liability hearing\n##### (a) Fraudulent material or statements\nIn the case that the Secretary of Health and Human Services determines that a vaccine manufacturer or vaccine sponsor has made fraudulent material or statements or concealed material information with respect to a situation described in this Act, or an amendment made by this Act, the Secretary shall and provide such manufacturer or sponsor 30 days to refute a determination made in a hearing described in subsection (b).\n##### (b) Hearing\n**(1) In general**\nThe Secretary shall determine a date, time, and format for a hearing under this subsection, including a requirement that the vaccine manufacturer or vaccine sponsor provide any requested document to the Secretary not more than five days before the hearing.\n**(2) Format**\nThe format of a hearing under paragraph (1) shall be determined by the Secretary.\n**(3) Publication**\nAny written or verbal testimony submitted by the vaccine manufacturer or vaccine sponsor at the hearing under paragraph (1) shall be published on the internet website of the Secretary of Health and Human Services.\n##### (c) Does not provide information\nIn the case that the vaccine manufacturer or vaccine sponsor does not respond to the Secretary in accordance with this section, an initial determination of fraud shall be maintained and shall have the full force and effect of this Act.",
      "versionDate": "2025-05-29",
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
        "updateDate": "2025-06-03T13:07:28Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3631ih.xml"
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
      "title": "VITAL Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VITAL Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Vaccines in Trial and Liability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To criminalize fraudulent statements made with respect to clinical vaccine trials.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:33:30Z"
    }
  ]
}
```
