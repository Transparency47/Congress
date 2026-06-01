# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3021?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3021
- Title: ENFORCE Act
- Congress: 119
- Bill type: S
- Bill number: 3021
- Origin chamber: Senate
- Introduced date: 2025-10-21
- Update date: 2025-12-18T16:15:12Z
- Update date including text: 2025-12-18T16:15:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-21: Introduced in Senate
- 2025-10-21 - IntroReferral: Introduced in Senate
- 2025-10-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-12-16 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8754-8755; text: CR S8754-8755)
- 2025-12-16 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-12-16 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-12-16 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-12-17 - Floor: Message on Senate action sent to the House.
- 2025-12-17 09:59:02 - Floor: Received in the House.
- 2025-12-17 10:22:12 - Floor: Held at the desk.
- Latest action: 2025-10-21: Introduced in Senate

## Actions

- 2025-10-21 - IntroReferral: Introduced in Senate
- 2025-10-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-12-16 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8754-8755; text: CR S8754-8755)
- 2025-12-16 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-12-16 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-12-16 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-12-17 - Floor: Message on Senate action sent to the House.
- 2025-12-17 09:59:02 - Floor: Received in the House.
- 2025-12-17 10:22:12 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-21",
    "latestAction": {
      "actionDate": "2025-10-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3021",
    "number": "3021",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "ENFORCE Act",
    "type": "S",
    "updateDate": "2025-12-18T16:15:12Z",
    "updateDateIncludingText": "2025-12-18T16:15:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-12-17",
      "actionTime": "10:22:12",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-12-17",
      "actionTime": "09:59:02",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S8754-8755; text: CR S8754-8755)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-10-21",
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
      "actionDate": "2025-10-21",
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
            "date": "2025-12-16T17:18:14Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-10-21T19:15:21Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CT"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "UT"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3021is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3021\nIN THE SENATE OF THE UNITED STATES\nOctober 21, 2025 Mr. Cornyn (for himself, Mr. Blumenthal , Mr. Lee , and Mr. Kennedy ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to enhance enforcement with respect to material depicting obscene child sexual abuse or constituting child pornography, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhancing Necessary Federal Offenses Regarding Child Exploitation Act or the ENFORCE Act .\n#### 2. Clarifying production with respect to material constituting or containing child pornography\nSection 2252A of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking paragraph (7) and inserting the following:\n(7) knowingly produces child pornography, as defined in section 2256(8)(C), that\u2014 (A) the person knows, or has reason to know, will be mailed, shipped, or transported using any means or facility of interstate or foreign commerce or in or affecting interstate or foreign commerce; (B) was produced using materials that have been mailed, shipped, or transported in or affecting interstate or foreign commerce; or (C) has been mailed, shipped, or transported using any means or facility of interstate or foreign commerce or in or affecting interstate or foreign commerce, ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking or (6) and inserting (6), or (7) ; and\n**(B)**\nby striking paragraph (3).\n#### 3. Enhancing enforcement with respect to obscene visual representations of child sexual abuse\n##### (a) Removing the statute of limitations for obscene visual representations of child sexual abuse\nSection 3299 of title 18, United States Code, is amended by inserting 1466A or before 1591 .\n##### (b) Including crimes of obscene visual representations of child sexual abuse in sex offender registration\nSection 111(5)(A)(iii) of the Adam Walsh Child Protection and Safety Act of 2006 ( 34 U.S.C. 20911(5)(A)(iii) ) is amended by inserting 1466A or before 1591 .\n##### (c) Prohibition on reproduction of obscene visual representations of child sexual abuse in discovery\nSection 1466A of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (f) as subsection (g); and\n**(2)**\nby inserting after subsection (e) the following:\n(f) Prohibition on reproduction of obscene visual depictions of child sexual abuse In any criminal proceeding brought under this section\u2014 (1) any visual depiction involved in a violation of this section shall remain in the care, custody, and control of either the Government or the court in the same manner specified for child pornography in paragraphs (1) and (2) of section 3509(m); and (2) any identifiable minor, as that term is defined in section 2256(9), depicted in any visual depiction involved in a violation of this section may have access to such depiction in the same manner specified for a victim, with respect to child pornography depicting the victim, in section 3509(m)(3). .\n##### (d) Presumption of detention for violations of section 1466A pending trial\nSection 3142 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (c)(1)(B), in the undesignated matter following clause (xiv), by striking that involves and all that follows through 2425 of this title and inserting that involves an offense described in subsection (e)(3)(E) ; and\n**(2)**\nin subsection (e)(3), by striking subparagraph (E) and inserting the following:\n(E) an offense\u2014 (i) involving a minor victim under section 1201, 1591, 2241(a), 2241(b), 2242, 2244(a)(1), 2245, 2421, or 2422(a) of this title; or (ii) under section 1466A(a), 2241(c), 2251A, 2252(a)(1), 2252(a)(2), 2252(a)(3), 2252A(a)(1), 2252A(a)(2), 2252A(a)(3), 2252A(a)(4), 2260, 2422(b), 2423, or 2425 of this title. .\n##### (e) Supervised release for violations of section 1466A after imprisonment\nSection 3583(k) of title 18, United States Code, is amended, in the first sentence, by inserting 1466A, before 1591, .",
      "versionDate": "2025-10-21",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3021es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 3021\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend title 18, United States Code, to enhance enforcement with respect to material depicting obscene child sexual abuse or constituting child pornography, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhancing Necessary Federal Offenses Regarding Child Exploitation Act or the ENFORCE Act .\n#### 2. Clarifying production with respect to material constituting or containing child pornography\nSection 2252A of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking paragraph (7) and inserting the following:\n(7) knowingly produces child pornography, as defined in section 2256(8)(C), that\u2014 (A) the person knows, or has reason to know, will be mailed, shipped, or transported using any means or facility of interstate or foreign commerce or in or affecting interstate or foreign commerce; (B) was produced using materials that have been mailed, shipped, or transported in or affecting interstate or foreign commerce; or (C) has been mailed, shipped, or transported using any means or facility of interstate or foreign commerce or in or affecting interstate or foreign commerce, ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking or (6) and inserting (6), or (7) ; and\n**(B)**\nby striking paragraph (3).\n#### 3. Enhancing enforcement with respect to obscene visual representations of child sexual abuse\n##### (a) Removing the statute of limitations for obscene visual representations of child sexual abuse\nSection 3299 of title 18, United States Code, is amended by inserting 1466A or before 1591 .\n##### (b) Including crimes of obscene visual representations of child sexual abuse in sex offender registration\nSection 111(5)(A)(iii) of the Adam Walsh Child Protection and Safety Act of 2006 (34 U.S.C. 20911(5)(A)(iii)) is amended by inserting 1466A or before 1591 .\n##### (c) Prohibition on reproduction of obscene visual representations of child sexual abuse in discovery\nSection 1466A of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (f) as subsection (g); and\n**(2)**\nby inserting after subsection (e) the following:\n(f) Prohibition on reproduction of obscene visual depictions of child sexual abuse In any criminal proceeding brought under this section\u2014 (1) any visual depiction involved in a violation of this section shall remain in the care, custody, and control of either the Government or the court in the same manner specified for child pornography in paragraphs (1) and (2) of section 3509(m); and (2) any identifiable minor, as that term is defined in section 2256(9), depicted in any visual depiction involved in a violation of this section may have access to such depiction in the same manner specified for a victim, with respect to child pornography depicting the victim, in section 3509(m)(3). .\n##### (d) Presumption of detention for violations of section 1466A pending trial\nSection 3142 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (c)(1)(B), in the undesignated matter following clause (xiv), by striking that involves and all that follows through 2425 of this title and inserting that involves an offense described in subsection (e)(3)(E) ; and\n**(2)**\nin subsection (e)(3), by striking subparagraph (E) and inserting the following:\n(E) an offense\u2014 (i) involving a minor victim under section 1201, 1591, 2241(a), 2241(b), 2242, 2244(a)(1), 2245, 2421, or 2422(a) of this title; or (ii) under section 1466A(a), 2241(c), 2251A, 2252(a)(1), 2252(a)(2), 2252(a)(3), 2252A(a)(1), 2252A(a)(2), 2252A(a)(3), 2252A(a)(4), 2260, 2422(b), 2423, or 2425 of this title. .\n##### (e) Supervised release for violations of section 1466A after imprisonment\nSection 3583(k) of title 18, United States Code, is amended, in the first sentence, by inserting 1466A, before 1591, .",
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
        "actionDate": "2025-08-01",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4831",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ENFORCE Act",
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
            "name": "Child safety and welfare",
            "updateDate": "2025-12-17T19:19:52Z"
          },
          {
            "name": "Crimes against children",
            "updateDate": "2025-12-17T19:20:18Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-12-17T19:20:12Z"
          },
          {
            "name": "Domestic violence and child abuse",
            "updateDate": "2025-12-17T19:20:00Z"
          },
          {
            "name": "Pornography",
            "updateDate": "2025-12-17T19:19:48Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-12-17T19:20:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-06T14:28:58Z"
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
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3021is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3021es.xml"
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
      "title": "ENFORCE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:20Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "ENFORCE Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-12-17T04:23:21Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Enhancing Necessary Federal Offenses Regarding Child Exploitation Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-12-17T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ENFORCE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-25T07:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Enhancing Necessary Federal Offenses Regarding Child Exploitation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-25T07:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to enhance enforcement with respect to material depicting obscene child sexual abuse or constituting child pornography, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-25T07:33:21Z"
    }
  ]
}
```
