# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1379?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1379
- Title: Trafficking Survivors Relief Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1379
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2026-04-07T19:59:31Z
- Update date including text: 2026-04-07T19:59:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1379",
    "number": "1379",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "F000478",
        "district": "7",
        "firstName": "Russell",
        "fullName": "Rep. Fry, Russell [R-SC-7]",
        "lastName": "Fry",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Trafficking Survivors Relief Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-07T19:59:31Z",
    "updateDateIncludingText": "2026-04-07T19:59:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
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
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
          "date": "2025-02-14T18:30:05Z",
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
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "CA"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "MO"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "GA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "MI"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "AZ"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "OH"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "OH"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "KS"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "AK"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NC"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "TX"
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
      "sponsorshipDate": "2025-11-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1379ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1379\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Fry (for himself, Mr. Lieu , Mrs. Wagner , and Mr. Garcia of California ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide for the vacating of certain convictions and expungement of certain arrests of victims of human trafficking.\n#### 1. Short title\nThis Act may be cited as the Trafficking Survivors Relief Act of 2025 .\n#### 2. Federal expungement for victims of trafficking\n##### (a) In general\nChapter 237 of title 18, United States Code, is amended by adding at the end the following:\n3771A. Motion to vacate; expungement; mitigating factors (a) Definitions In this section\u2014 (1) the term child means an individual who has not attained 18 years of age; (2) the term covered prisoner means an individual who\u2014 (A) was convicted of a level A offense or level B offense; (B) was sentenced to a term of imprisonment for the offense described in subparagraph (A); and (C) is imprisoned under such term of imprisonment; (3) the terms employee and officer have the meanings given the terms in section 2105 of title 5; (4) the term Federal offense means an offense that is punishable under Federal law; (5) the term level A offense means a Federal offense that is not a violent crime; (6) the term level B offense \u2014 (A) means a Federal offense that is a violent crime; and (B) does not include a Federal offense that is a violent crime of which a child was a victim; (7) the term level C offense means any Federal offense that is not a level A offense; (8) the term victim of trafficking has the meaning given that term in section 103 of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102 ); and (9) the term violent crime has the meaning given that term in section 103 of the Juvenile Justice and Delinquency Prevention Act of 1974 ( 34 U.S.C. 11103 ). (b) Motions To vacate convictions or expunge arrests (1) In general (A) Convictions of level A offenses A person convicted of any level A offense (or an attorney representing such a person) may move the court that imposed the sentence for the level A offense to vacate the judgment of conviction if the level A offense was committed as a direct result of the person having been a victim of trafficking. (B) Arrests for level A offenses A person arrested for any level A offense (or an attorney representing such a person) may move the district court of the United States for the district and division embracing the place where the person was arrested to expunge all records of the arrest if the conduct or alleged conduct of the person that resulted in the arrest was directly related to the person having been a victim of trafficking. (C) Arrests for level C offenses A person arrested for any level C offense (or an attorney representing such a person) may move the district court of the United States for the district and division embracing the place where the person was arrested to expunge all records of the arrest if\u2014 (i) the conduct or alleged conduct of the movant that resulted in the arrest was directly related to the movant having been a victim of trafficking; and (ii) (I) the movant was acquitted of the level C offense; (II) the Government did not pursue, or the Government moved to dismiss, criminal charges against the movant for the level C offense; or (III) (aa) the charges against the movant for the level C offense were reduced to an offense that is a level A offense; and (bb) the movant was acquitted of the level A offense, the Government did not pursue, or the Government moved to dismiss, criminal charges against the movant for the level A offense, or any subsequent conviction of the level A offense was vacated. (2) Contents of motion A motion described in paragraph (1) shall\u2014 (A) be in writing; (B) describe any supporting evidence; (C) state the offense; and (D) include copies of any documents showing that the movant is entitled to relief under this section. (3) Hearing (A) Mandatory hearing (i) Motion in opposition Not later than 30 days after the date on which a motion is filed under paragraph (1), the Government may file a motion in opposition of the motion filed under paragraph (1). (ii) Mandatory hearing If the Government files a motion described in clause (i), not later than 15 days after the date on which the motion is filed, the court shall hold a hearing on the motion. (B) Discretionary hearing If the Government does not file a motion described in subparagraph (A)(i), the court may hold a hearing on the motion not later than 45 days after the date on which a motion is filed under paragraph (1). (4) Factors (A) Vacating convictions of level A offenses The court may grant a motion under paragraph (1)(A) if, after notice to the Government and an opportunity to be heard, the court finds, by a preponderance of the evidence, that\u2014 (i) the movant was convicted of a level A offense; and (ii) the participation in the level A offense by the movant was a direct result of the movant having been a victim of trafficking. (B) Expunging arrests for level A offenses The court may grant a motion under paragraph (1)(B) if, after notice to the Government and an opportunity to be heard, the court finds, by a preponderance of the evidence, that\u2014 (i) the movant was arrested for a level A offense; and (ii) the conduct or alleged conduct that resulted in the arrest was directly related to the movant having been a victim of trafficking. (C) Expunging arrests for level C offenses The court may grant a motion under paragraph (1)(C) if, after notice to the Government and an opportunity to be heard, the court finds, by a preponderance of the evidence, that\u2014 (i) the movant was arrested for a level C offense and the conduct or alleged conduct that resulted in the arrest was directly related to the movant having been a victim of trafficking; and (ii) (I) the movant was acquitted of the level C offense; (II) the Government did not pursue, or the Government moved to dismiss, criminal charges against the movant for the level C offense; or (III) (aa) the charges against the movant for the level C offense were reduced to a level A offense; and (bb) the movant was acquitted of the level A offense, the Government did not pursue, or the Government moved to dismiss, criminal charges against the movant for the level A offense, or any subsequent conviction of that level A offense was vacated. (5) Supporting evidence (A) In general For purposes of this section, in determining whether the movant is a victim of trafficking, the court shall consider an affidavit or sworn testimony of a licensed anti-human trafficking service provider or clinician. The court may consider any supporting evidence the court determines is of sufficient credibility and probative value, including sworn testimony from a law enforcement officer detailing the role of the movant in coercing other victims into committing Federal offenses. (B) Affidavit or sworn testimony sufficient evidence The affidavit or sworn testimony described in subparagraph (A) shall be sufficient evidence to vacate a conviction or expunge an arrest under this section if the court determines that\u2014 (i) the affidavit or sworn testimony is credible; and (ii) no other evidence is readily available. (6) Conviction or arrest of other persons not required It shall not be necessary that any person other than the movant be convicted of or arrested for an offense before the movant may file a motion under paragraph (1). (7) Denial of motion (A) In general If the court denies a motion filed under paragraph (1), the denial shall be final, subject to the discovery of any new and compelling evidence or information. (B) Reasons for denial If the court denies a motion filed under paragraph (1), the court shall state the reasons for the denial in writing. (C) Reasonable time to cure deficiencies in motion If the motion was denied due to a curable deficiency in the motion, the court shall allow the movant sufficient time to cure the deficiency. (8) Appeal An order granting or denying a motion under this section may be appealed in accordance with section 1291 of title 28. (c) Vacatur of convictions (1) In general If the court grants a motion to vacate a conviction of a level A offense under subsection (b), the court shall immediately\u2014 (A) vacate the conviction for cause; (B) set aside the verdict and enter a judgment of acquittal; and (C) enter an expungement order that directs that there be expunged from all official records all references to\u2014 (i) the arrest of the movant for the level A offense; (ii) the institution of criminal proceedings against the movant relating to the level A offense; and (iii) the results of the proceedings. (2) Limitation Nothing in this subsection requires a court to amend, impose, or remove any fine or restitution order in a criminal or civil proceeding. (3) Effect If a conviction is vacated under an order entered under paragraph (1) the conviction shall not be regarded as a conviction under Federal law and the movant for whom the conviction was vacated shall be considered to have the status occupied by the movant before the arrest or the institution of the criminal proceedings related to such conviction. (d) Expungement of arrests (1) In general If the court grants a motion to expunge all records of an arrest for an offense under subsection (b), the court shall immediately enter an expungement order that directs that there be expunged from all official records all references to\u2014 (A) the arrest of the movant for the offense; (B) the institution of any criminal proceedings against the movant relating to the offense; and (C) the results of the proceedings, if any. (2) Effect If an arrest is expunged under an order entered under paragraph (1) the arrest shall not be regarded as an arrest under Federal law and the movant for whom the arrest is expunged shall be considered to have the status occupied by the movant before the arrest or the institution of the criminal proceedings related to such arrest, if any. (e) Mitigating factors (1) In general The court that imposed sentence for a level A offense or level B offense upon a covered prisoner may reduce the term of imprisonment for the offense\u2014 (A) upon\u2014 (i) motion by the covered prisoner or the Director of the Bureau of Prisons; or (ii) the court's own motion; (B) after notice to the Government; (C) after considering\u2014 (i) the factors set forth in section 3553(a); (ii) the nature and seriousness of the danger to any person, if applicable; and (iii) the community, or any crime victims; and (D) if the court finds, by a preponderance of the evidence, that the covered prisoner committed the offense as a direct result of the covered prisoner having been a victim of trafficking. (2) Requirement Any proceeding under this subsection shall be subject to section 3771. (3) Particularized inquiry For any motion under paragraph (1), the Government shall conduct a particularized inquiry of the facts and circumstances of the original sentencing of the covered prisoner in order to assess whether a reduction in sentence would be consistent with this section. (f) Additional actions by court The court shall, upon granting a motion under this section, take any additional action necessary to grant the movant full relief. (g) No fees A person may not be required to pay a filing fee, service charge, copay fee, processing fee, or any other charge for filing a motion under this section. (h) Confidentiality of movant (1) In general A motion under this section and any documents, pleadings, or orders relating to the motion shall be filed under seal. (2) Information not available for public inspection An officer or employee may not make available for public inspection any report, paper, picture, photograph, court file, or other document, in the custody or possession of the officer or employee, that identifies the movant. (i) Applicability This section shall apply to any conviction or arrest occurring before, on, or after the date of enactment of this section. .\n##### (b) Technical and conforming amendment\nThe table of sections of chapter 237 of title 18, United States Code, is amended by adding at the end the following:\n3771A. Motion to vacate; expungement; mitigating factors. .\n#### 3. Reports\n##### (a) United States Attorney motions for vacatur or expungement\nNot later than 1 year after the date of enactment of this Act, each United States attorney shall submit to the Attorney General a report that details\u2014\n**(1)**\nthe number of motions for vacatur or expungement filed under section 3771A of title 18, United States Code, as added by section 2, in the district of the United States attorney; and\n**(2)**\nfor each motion described in paragraph (1)\u2014\n**(A)**\nthe underlying offense;\n**(B)**\nthe response of the United States attorney to the motion; and\n**(C)**\nthe final determination of the court with respect to the motion.\n##### (b) United States attorney training on human trafficking indicators\nNot later than 1 year after the date of enactment of this Act, the Attorney General shall submit to Congress a report that details all professional training received by United States attorneys on indicators of human trafficking during the preceding 12-month period.\n##### (c) Government Accountability Office\nNot later than 3 years after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress a report that\u2014\n**(1)**\nassesses the impact of the enactment of section 3771A of title 18, United States Code, as added by section 2; and\n**(2)**\nincludes\u2014\n**(A)**\nthe number of human trafficking survivors who have filed motions for vacatur or expungement under such section 3771A;\n**(B)**\nthe final determination of each court that adjudicated a motion described in subparagraph (A);\n**(C)**\nrecommendations to increase access to post-conviction relief for human trafficking survivors with Federal criminal records; and\n**(D)**\nrecommendations for improving the implementation and tracking of professional training of United States attorneys on indicators of human trafficking.\n#### 4. Use of grants for post-conviction relief representation\nThe Office of Justice Programs or the Office on Violence Against Women, in awarding a grant that may be used for legal representation, may not prohibit a recipient from using the grant for legal representation for post-conviction relief.\n#### 5. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthis Act is a first step to address the changing tactics of human traffickers, who are using forced criminality as a form of force, fraud, and coercion in their human trafficking enterprises; and\n**(2)**\nCongress is committed to continuing to find solutions as needed to thwart human traffickers and protect survivors of human trafficking.\n#### 6. Human trafficking defense\n##### (a) In general\nChapter 1 of title 18, United States Code, is amended by adding at the end the following:\n28. Human trafficking defense (a) Definition In this section, the term covered Federal offense means a level A offense or level B offense, as those terms are defined in section 3771A. (b) Presumption of duress In a prosecution for a covered Federal offense, a defendant who establishes by clear and convincing evidence that the defendant was a victim of trafficking at the time at which the defendant committed the offense shall create a rebuttable presumption that the offense was induced by duress. (c) Record or proceeding under seal In any proceeding in which a defense under subsection (b) is raised, any record or part of the proceeding related to the defense shall, on motion, be placed under seal until such time as a conviction is entered for the offense. (d) Post-Conviction relief A failure to assert, or failed assertion of, a defense under subsection (b) by an individual who is convicted of a covered Federal offense may not preclude the individual from asserting as a mitigating factor, at sentencing or in a proceeding for any post-conviction relief, that at the time of the commission of the offense, the defendant was a victim of trafficking and committed the offense under duress. (e) Federal aid A failure to assert, or failed assertion of, a defense under subsection (b) by an individual who is convicted of a covered Federal offense may not be used for the purpose of disqualifying the individual from participating in any federally funded program that aids victims of human trafficking. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 1 of title 18, United States Code, is amended by adding at the end the following:\n28. Human trafficking defense. .\n#### 7. Rule of construction\nNothing in this Act, or the amendments made by this Act, may be construed to conflict with any of the crime victims\u2019 rights described in section 3771 of title 18, United States Code.",
      "versionDate": "2025-02-14",
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
        "actionDate": "2025-07-10",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2255",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Trafficking Survivors Relief Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-23",
        "text": "Became Public Law No: 119-73."
      },
      "number": "4323",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Trafficking Survivors Relief Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-07-08T12:59:59Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-07-08T12:59:59Z"
          },
          {
            "name": "Criminal justice information and records",
            "updateDate": "2025-07-08T12:59:59Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-07-08T12:59:59Z"
          },
          {
            "name": "Evidence and witnesses",
            "updateDate": "2025-07-08T12:59:59Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-08T12:59:59Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-07-08T12:59:59Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2025-07-08T12:59:59Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2025-07-08T12:59:59Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2025-07-08T12:59:59Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2025-07-08T12:59:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-14T12:48:53Z"
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
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1379ih.xml"
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
      "title": "Trafficking Survivors Relief Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Trafficking Survivors Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the vacating of certain convictions and expungement of certain arrests of victims of human trafficking.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:19:03Z"
    }
  ]
}
```
