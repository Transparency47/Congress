# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3645?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3645
- Title: Deportation Acceleration Act
- Congress: 119
- Bill type: S
- Bill number: 3645
- Origin chamber: Senate
- Introduced date: 2026-01-14
- Update date: 2026-02-10T18:12:24Z
- Update date including text: 2026-02-10T18:12:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in Senate
- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-01-14: Introduced in Senate

## Actions

- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3645",
    "number": "3645",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Deportation Acceleration Act",
    "type": "S",
    "updateDate": "2026-02-10T18:12:24Z",
    "updateDateIncludingText": "2026-02-10T18:12:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-14",
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
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T21:29:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3645is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3645\nIN THE SENATE OF THE UNITED STATES\nJanuary 14, 2026 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo improve the efficiency of the removal process by enhancing cooperation between government entities and by expanding the grounds for deportation for any alien to include any felony or any 2 misdemeanors.\n#### 1. Short title\nThis Act may be cited as the Deportation Acceleration Act .\n#### 2. Mandatory real-Time data sharing of criminal convictions\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Attorney General, in consultation with the Secretary of Homeland Security, shall establish a process for State and local courts and law enforcement agencies to report every criminal conviction of any individual who is not a United States citizen to the Department of Homeland Security not later than 24 hours after entering such conviction through integration with existing Federal databases, including the database that was used by Secure Communities.\n##### (b) Removal proceedings\nUpon receiving information about a criminal conviction of a noncitizen that renders such noncitizen removable under section 237(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2) ), the Secretary of Homeland Security shall initiate removal proceedings by issuing a Notice to Appear (Form I\u2013862) to such noncitizen or an immigration detainer to the State or local law enforcement agency that has custody of such noncitizen.\n#### 3. Expanded use of expedited removal\nSection 238 of the Immigration and Nationality Act ( 8 U.S.C. 1228 ) is amended\u2014\n**(1)**\nby striking the section header and inserting the following: Expedited removal of any noncitizen convicted of a felony or 2 misdemeanors. ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the paragraph heading, by striking in and inserting In ; and\n**(ii)**\nby striking any criminal offense covered in section 241(a)(2)(A)(iii), (B), (C), or (D), or any offense covered by section 241(a)(2)(A)(ii) for which both predicate offenses are, without regard to the date of their commission, otherwise covered by section 241(a)(2)(A)(i) and inserting any felony or 2 misdemeanors ;\n**(B)**\nby moving paragraphs (2), (3), and (4) 2 ems to the right;\n**(C)**\nin paragraph (2)\u2014\n**(i)**\nby striking an aggravated felony and inserting a felony or 2 misdemeanors ; and\n**(ii)**\nby striking felon and inserting alien ;\n**(D)**\nin paragraph (3)\u2014\n**(i)**\nin the paragraph heading, by striking expedited and inserting Expedited ; and\n**(ii)**\nin subparagraph (A), by striking an aggravated felony before the alien's release from incarceration for the underlying aggravated felony and inserting a felony or 2 misdemeanors before the alien's release from incarceration for the underlying crime ; and\n**(E)**\nin paragraph (4), in the paragraph heading, by striking review and inserting Review ;\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin the subsection header, by striking Who Are Not Permanent Residents ;\n**(B)**\nby striking paragraphs (1) and (2) and inserting the following:\n(1) In general The Attorney General may determine the deportability of an alien who has been convicted of a felony or 2 misdemeanors and issue an order of removal pursuant to the procedures set forth in this subsection or in section 240. ; and\n**(C)**\nby redesignating paragraphs (3), (4), and (5) as paragraphs (2), (3), and (4), respectively;\n**(4)**\nin the first subsection (c), by striking an aggravated felony and inserting a felony or 2 misdemeanors ; and\n**(5)**\nby redesignating the second subsection (c) as subsection (d).\n#### 4. Shortened appeal windows in non-Asylum removal cases\nSection 240 of the Immigration and Nationality Act (8 U.S..C. 1229a) is amended\u2014\n**(1)**\nin subsection (a), by adding at the end the following:\n(4) Prioritization of criminal removal cases The Attorney General shall\u2014 (A) prioritize criminal removal cases on immigration court dockets; and (B) issue regulations to ensure, to the maximum extent practicable, appeals in such cases are resolved not later than 120 days after the relevant petition is filed. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2)(A), in the matter preceding clause (i), by striking The proceeding and inserting Except as provided in subparagraphs (B) and (C), the proceeding ; and\n**(B)**\nin paragraph (5)(C), by striking 180 days and inserting 30 days ; and\n**(3)**\nin subsection (c)(7)(C)(i), by striking 90 days and inserting 30 days .\n#### 5. Cooperation incentives and highway funds penalties for sanctuary jurisdictions\n##### (a) Defined term\nIn this section, the term sanctuary jurisdiction means any State or political subdivision of a State that has in effect any law, policy, or practice that prohibits or restricts government entities or officials from\u2014\n**(1)**\nsharing citizenship or immigration status information with the Department of Homeland Security; or\n**(2)**\ncomplying with detainers or notification requests issued by the Department of Homeland Security.\n##### (b) Cooperation incentives\n**(1) Authorization of appropriations**\nThere is authorized to be appropriated to the Department of Homeland Security $150,000,000 for fiscal year 2026 and every subsequent fiscal year annually for competitive grants to be awarded to States and local governments that fully cooperate with immigration detainers, agreements authorized under section 287(g) of the Immigration and Nationality Act ( 8 U.S.C. 1357(g) ), and information sharing.\n**(2) Use of grant funds**\nGrant funds awarded pursuant to paragraph (1) may be used for detention capacity, officer training, and enforcement equipment.\n##### (c) Penalties\n**(1) In general**\nBeginning on the first day of the first fiscal year beginning after the date of the enactment of this Act, the Secretary of Transportation, except as provided under paragraph (2), shall withhold 15 percent of the funds a sanctuary jurisdiction would otherwise receive from the Highway Trust Fund apportionment in the relevant fiscal year unless the sanctuary jurisdiction certifies to the Secretary of Homeland Security that it no longer meets the definition of sanctuary jurisdiction under paragraph (1).\n**(2) Grace period; appeals**\nNotwithstanding paragraph (1)\u2014\n**(A)**\neach sanctuary jurisdictions shall be given 180 days from the date of notification that funding from the Highway Trust Fund will be withheld to submit the certification described in paragraph (1); and\n**(B)**\nsanctuary jurisdictions may appeal a withholding determination to the Attorney General on grounds of undue hardship.\n#### 6. Applicability\nThe expedited removal of aliens convicted of a felony or 2 misdemeanors authorized under section 238 of the Immigration and Nationality Act, as amended by section 3, shall apply regardless of whether the acts constituting the elements of the relevant crimes or the conviction for such crimes occurred before, on, or after the date of the enactment of this Act.",
      "versionDate": "2026-01-14",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-02-10T18:12:24Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3645is.xml"
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
      "title": "Deportation Acceleration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Deportation Acceleration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the efficiency of the removal process by enhancing cooperation between government entities and by expanding the grounds for deportation for any alien to include any felony or any 2 misdemeanors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T05:48:33Z"
    }
  ]
}
```
