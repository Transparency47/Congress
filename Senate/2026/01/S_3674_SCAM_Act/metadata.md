# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3674?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3674
- Title: SCAM Act
- Congress: 119
- Bill type: S
- Bill number: 3674
- Origin chamber: Senate
- Introduced date: 2026-01-15
- Update date: 2026-03-19T11:03:28Z
- Update date including text: 2026-03-19T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in Senate
- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - Calendars: Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time.
- 2026-01-26 - Calendars: Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 301.
- Latest action: 2026-01-15: Introduced in Senate

## Actions

- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - Calendars: Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time.
- 2026-01-26 - Calendars: Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 301.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3674",
    "number": "3674",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "SCAM Act",
    "type": "S",
    "updateDate": "2026-03-19T11:03:28Z",
    "updateDateIncludingText": "2026-03-19T11:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-26",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 301.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time.",
      "type": "Calendars"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-15",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "FL"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "SC"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-01-28",
      "state": "UT"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2026-01-28",
      "state": "TN"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "MT"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "LA"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "WY"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "FL"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3674pcs.xml",
      "text": "II\nCalendar No. 301\n119th CONGRESS\n2d Session\nS. 3674\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2026 Mr. Schmitt introduced the following bill; which was read the first time\nJanuary 26, 2026 Read the second time and placed on the calendar\nA BILL\nTo expand and clarify the grounds for civil denaturalization proceedings for individuals who have defrauded a governmental program, joined a terrorist organization, or committed certain criminal offenses.\n#### 1. Short titles\nThis Act may be cited as the Stop Citizenship Abuse and Misrepresentation Act or the SCAM Act .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nBecoming a naturalized United States citizen means not only having the right to live and work in the United States and gaining access to various social, economic, and political benefits, but also accepting sacred duties and obligations to our Nation.\n**(2)**\nIn recent years, many naturalized citizens have betrayed those sacred duties and obligations, eschewed responsible citizenship, and instead viewed their new citizenship status as a purely administrative benefit granting them access to privileges, immunities, and benefits they can leverage for their own personal gain.\n**(3)**\nNaturalization is a long-standing, time-honored, and essential American tradition.\n**(4)**\nAn applicant wishing to become a citizen of the United States must demonstrate, at the time of naturalization, that he or she is\u2014\n**(A)**\na person of good moral character;\n**(B)**\nattached to the principles of the Constitution of the United States; and\n**(C)**\nwell disposed to the good order and happiness of the United States.\n**(5)**\nAny person who has been convicted of fraud against a governmental program demonstrates moral turpitude and any person who has been convicted of fraud against a governmental program after being extended the privilege of United States citizenship demonstrates, both at the time of such conviction and at the time of his or her naturalization, that he or she is not and was not\u2014\n**(A)**\na person of good moral character;\n**(B)**\nattached to the principles of the Constitution of the United States; and\n**(C)**\nwell disposed to the good order and happiness of the United States.\n**(6)**\nAny person who affiliates with a foreign terrorist organization, such as a drug cartel, or engages in espionage puts our Nation's security at great risk of degradation and any person who affiliates with a foreign terrorist organization or engages in espionage after being extended the privilege of United States citizenship demonstrates, both at the time of such affiliation or espionage and at the time of his or her naturalization, that he or she is not and was not\u2014\n**(A)**\na person of good moral character;\n**(B)**\nattached to the principles of the Constitution of the United States; and\n**(C)**\nwell disposed to the good order and happiness of the United States.\n**(7)**\nAny alien who has been convicted of an aggravated felony is deportable and designated as permanently ineligible for naturalization and any person who has been convicted of an aggravated felony after being extended the privilege of United States citizenship demonstrates, both at the time of such conviction and at the time of his or her naturalization, that he or she is not and was not\u2014\n**(A)**\na person of good moral character;\n**(B)**\nattached to the principles of the Constitution of the United States; and\n**(C)**\nwell disposed to the good order and happiness of the United States.\n**(8)**\nAs the Supreme Court has noted: An alien has no moral nor constitutional right to retain the privileges of citizenship if, by false evidence or the like, an imposition has been practiced upon the court, without which the certificate could not and would not have been issued. (Johannessen v. United States, 225 U.S. 227, 241 (1912)).\n**(9)**\nThe Supreme Court has also explained: No alien has the slightest right to naturalization unless all statutory requirements are complied with; and every certificate of citizenship must be treated as granted upon condition that the government may challenge it . . . and demand its cancelation unless issued in accordance with such requirements. If procured when prescribed qualifications have no existence in fact, it is illegally procured . . . . (United States v. Ginsberg, 243 U.S. 472, 475 (1917)).\n##### (b) Sense of Congress\nIt is the sense of Congress that the Supreme Court, in Costello v. INS, 376 U.S. 120 (1964), misconstrued the effects of denaturalization under section 340 of the Immigration and Nationality Act ( 8 U.S.C. 1451 ) for the reasons stated in the concurring opinion in Castillo v. Bondi, 140 F.4th 777 (6th Cir. 2025) (Thapar, J., concurring).\n#### 3. Purpose\nThe purpose of this Act is to expand and clarify the grounds for the United States to pursue civil denaturalization proceedings against individuals who have proven, by defrauding a governmental program, affiliating with a foreign terrorist organization, or committing certain criminal offenses, that, at the time they were naturalized, they lacked the good moral character, attachment to the Constitution of the United States, and disposition to the good order and happiness of the United States that our Nation demands of those who desire to become naturalized citizens.\n#### 4. Expanding and clarifying denaturalization for individuals who lack good moral character and an attachment to the Constitution of the United States and are not well disposed to the good order and happiness of the United States\nSection 340 of the Immigration and Nationality Act ( 8 U.S.C. 1451 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting the Attorney General or after It shall be the duty of ;\n**(2)**\nby redesignating subsections (d), (e), (f), (g), and (h) as subsections (i), (j), (k), (l), and (m), respectively; and\n**(3)**\nby inserting after subsection (c) the following:\n(d) Membership in foreign terrorist organization If a person, during the 10-year period beginning on the date on which he or she was naturalized under this chapter, associates with, conspires with, aids, or abets any foreign terrorist organization (as designated under section 219(a)), such action shall be considered prima facie and sufficient evidence that\u2014 (1) such person, at the time of his or her naturalization\u2014 (A) was not a person of good moral character; (B) was not attached to the principles of the Constitution of the United States; and (C) was not well disposed to the good order and happiness of the United States; (2) the order admitting such person to citizenship\u2014 (A) was obtained by concealment of a material fact or by willful misrepresentation; and (B) shall be revoked and set aside, along with the cancellation of his or her certificate of naturalization; and (3) such revocation and setting aside of such admission order and such cancellation of such certificate of naturalization shall be effective as of the original date of such order and certificate, respectively. (e) Defrauding Federal, State, local, or tribal governments If a person who has been naturalized under this chapter is convicted of, admits to having committed, or admits to committing acts constituting the essential elements of, an offense involving fraud, an attempt to defraud, or conspiracy to defraud the Federal Government, a State government, a local government, or a tribal government (such as defrauding the United States Government of a Federal public benefit (as defined in section 401 of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1611(c) ) or defrauding a State or local government of a State or local public benefit (as defined in section 411(c) of such Act ( 8 U.S.C. 1621(c) )), of at least $10,000, and any act or acts leading to such conviction or admission began or occurred during the 10-year period beginning on the date of his or her naturalization, such conviction or admission shall be considered prima facie and sufficient evidence that\u2014 (1) such person, at the time of his or her naturalization\u2014 (A) was not a person of good moral character; (B) was not attached to the principles of the Constitution of the United States; and (C) was not well disposed to the good order and happiness of the United States; (2) the order admitting such person to citizenship\u2014 (A) was obtained by concealment of a material fact or by willful misrepresentation; and (B) shall be revoked and set aside, along with the cancellation of his or her certificate of naturalization; and (3) such revocation and setting aside of such admission order and such cancellation of such certificate of naturalization shall be effective as of the original date of such order and certificate, respectively. (f) Committing an aggravated felony or espionage offense If a person who has been naturalized under this chapter is convicted of, admits to having committed, or admits to committing acts constituting the essential elements of, an aggravated felony or espionage offense (including any offense described in section 792, 793, 794, 795, 796, 797, 798, 951, 1030(a)(1), 1831, 1832, 2152, 2153, 2154, 2155, or 2156 of title 18, United States Code; or an offense described in section 783 or 3121 of title 50, United States Code), and any act or acts leading to such conviction or admission began or occurred during the 10-year period beginning on the date on which he or she was naturalized, such conviction or admission shall be considered prima facie and sufficient evidence that\u2014 (1) such person, at the time of his or her naturalization\u2014 (A) was not a person of good moral character; (B) was not attached to the principles of the Constitution of the United States; and (C) was not well disposed to the good order and happiness of the United States; (2) the order admitting such person to citizenship\u2014 (A) was obtained by concealment of a material fact or by willful misrepresentation; and (B) shall be revoked and set aside, along with the cancellation of his or her certificate of naturalization; and (3) such revocation and setting aside of such admission order and such cancellation of such certificate of naturalization shall be effective as of the original date of such order and certificate, respectively. (g) Fallback provision If the 10-year period set forth in subsection (d), (e), or (f) is held to be unconstitutional or constitutionally insufficient by final judicial decision, for purposes of interpreting this Act\u2014 (1) such 10-year period shall be deemed to be a 5-year period, consistent with the published judicial opinion in Luria v. United States, 231 U.S. 27 (1913); and (2) every court of the United States shall construe such period to be 5 years. (h) Effects of denaturalization (1) Effective date The revocation and setting aside of a person\u2019s admission order and cancellation of the person\u2019s certificate of naturalization under this section shall be effective as of the original date of such order and certificate, respectively. Such denaturalization shall have retroactive effect, and the certificate of naturalization shall be treated as void from the date on which it was issued. (2) Removability Any person whose certificate of naturalization is cancelled under this section shall be removable pursuant to expedited proceedings described in section 238, regardless of\u2014 (A) the person\u2019s immigration status after denaturalization; and (B) the time that has elapsed since the date on which such person was naturalized. .\n#### 5. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such a provision or amendment to any particular person or circumstance is held to be unconstitutional, the remaining provisions of this Act and amendments made by this Act, and the application of such provisions and amendments to any other person or circumstance, shall not be affected.",
      "versionDate": "2026-01-26",
      "versionType": "Placed on Calendar Senate"
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
        "actionDate": "2026-01-20",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "7156",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SCAM Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2026-01-28T14:23:07Z"
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
      "date": "2026-01-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3674pcs.xml"
        }
      ],
      "type": "Placed on Calendar Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "SCAM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:28Z"
    },
    {
      "billTextVersionCode": "PCS",
      "billTextVersionName": "Placed on Calendar Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "SCAM Act",
      "titleType": "Short Title(s) from PCS (Placed on Senate Calendar) bill text",
      "titleTypeCode": "152",
      "updateDate": "2026-01-27T18:53:20Z"
    },
    {
      "billTextVersionCode": "PCS",
      "billTextVersionName": "Placed on Calendar Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Stop Citizenship Abuse and Misrepresentation Act",
      "titleType": "Short Title(s) from PCS (Placed on Senate Calendar) bill text",
      "titleTypeCode": "152",
      "updateDate": "2026-01-27T18:53:20Z"
    },
    {
      "title": "A bill to expand and clarify the grounds for civil denaturalization proceedings for individuals who have defrauded a governmental program, joined a terrorist organization, or committed certain criminal offenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T11:56:20Z"
    }
  ]
}
```
