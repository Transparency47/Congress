# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3114?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3114
- Title: Clean Slate Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3114
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2025-12-05T21:47:52Z
- Update date including text: 2025-12-05T21:47:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3114",
    "number": "3114",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001208",
        "district": "6",
        "firstName": "Lucy",
        "fullName": "Rep. McBath, Lucy [D-GA-6]",
        "lastName": "McBath",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Clean Slate Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:47:52Z",
    "updateDateIncludingText": "2025-12-05T21:47:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:01:30Z",
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
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "TX"
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
      "sponsorshipDate": "2025-07-10",
      "state": "OH"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "DE"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "AL"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3114ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3114\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mrs. McBath (for herself and Mr. Moran ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require automatic sealing of certain criminal records, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clean Slate Act of 2025 .\n#### 2. Sealing of certain records\n##### (a) Amendment\nSubchapter A of chapter 227 of title 18, United States Code, is amended by adding at the end the following:\n3560. Automatic sealing of certain records (a) Definitions In this section\u2014 (1) the term covered individual means an individual who\u2014 (A) is not a sex offender; (B) has been\u2014 (i) arrested for a Federal offense for which the individual was not convicted; or (ii) convicted of an offense under section 404 of the Controlled Substances Act ( 21 U.S.C. 844 ) or any Federal nonviolent offense involving marijuana; (C) in the case of a conviction described in subparagraph (B)(ii), has fulfilled each requirement of the sentence for the offense, including\u2014 (i) completing each term of imprisonment, probation, or supervised release; and (ii) satisfying each condition of imprisonment, probation, or supervised release; and (D) has not been convicted for any offense related to treason, terrorism, access and transmission of sensitive defense information, or other national security related convictions; (2) the term marijuana has the meaning given the term marihuana in section 102 of the Controlled Substances Act ( 21 U.S.C. 802 ); (3) the term nonviolent offense means an offense that is not\u2014 (A) murder; (B) voluntary manslaughter; (C) kidnapping; (D) aggravated assault; (E) a forcible sex offense; (F) robbery; (G) arson; (H) extortion; (I) the use or unlawful possession of\u2014 (i) a firearm, as defined in section 5845(a) of the Internal Revenue Code of 1986; or (ii) explosive materials, as defined in section 841(c); (J) a sex offense (as that term is defined in section 111 of the Sex Offender Registration and Notification Act ( 34 U.S.C. 20911 )); (K) torture, in violation of section 2340A; (L) interstate domestic violence, in violation of section 2261; (M) an offense under chapter 77; or (N) an attempt or conspiracy to commit an offense described in subparagraphs (A) through (M); and (4) the term sex offender has the meaning given the term in section 111 of the Adam Walsh Child Protection and Safety Act of 2006 ( 34 U.S.C. 20911 ). (b) Automatic sealing for certain arrests and nonviolent offenses (1) In general At the time of sentencing of a covered individual for a conviction for an offense pursuant to section 404 of the Controlled Substances Act ( 21 U.S.C. 844 ) or any Federal nonviolent offense involving marijuana, the court shall enter an order that each record and portion thereof that relates to the offense shall be sealed automatically on the date that is 1 year after the covered individual fulfills each requirement of the sentence, including\u2014 (A) completing each term of imprisonment, probation, or supervised release; and (B) satisfying each condition of imprisonment, probation, or supervised release. (2) Acquittal; determination not to file charges (A) Acquittal Not later than 60 days after the date on which a covered individual is acquitted, exonerated, or otherwise subject to a judgment which did not result in a conviction for a Federal offense, each record or portion thereof that relates to the Federal offense shall be sealed automatically. (B) Determination not to file charges (i) In general If a covered individual is arrested for a Federal offense and the Government does not file charges against the covered individual in relation to the Federal offense before the date that is 180 days after the date on which the arrest was made, each record or portion thereof that relates to the arrest and Federal offense shall be sealed automatically on such date. (ii) Unsealing for filing of charges At the request of the Government, a court may unseal a record sealed under clause (i) in order for the Government to file charges against the covered individual in relation to the Federal offense described in clause (i). (iii) Limitation If a record is unsealed under clause (ii), the record may only be resealed in accordance with paragraph (1) or subparagraph (A) of this paragraph. (c) Effect of sealing order (1) Protection from access Except as provided in paragraph (4), a record that has been sealed under this section or section 3560A shall not be accessible to any person. (2) Protection from perjury laws (A) In general Except as provided in subparagraph (B), an individual whose record has been sealed pursuant to this section shall not be required to disclose the existence of or any information contained in the individual\u2019s sealed record, and shall not be subject to prosecution under any civil or criminal provision of Federal or State law relating to perjury, false swearing, or making a false statement, including under section 1001, 1621, 1622, or 1623, for failing to recite or acknowledge any information that has been sealed with respect to the offense, or respond to any inquiry made of the individual, relating to the protected information. (B) Exception An individual whose record has been sealed pursuant to this section shall disclose information contained in such record\u2014 (i) when testifying in court; (ii) in the course of questioning by a law enforcement officer in connection with a subsequent criminal investigation; or (iii) in connection with employment described in subclauses (I) through (IV) of paragraph (4)(A)(ii) that the individual is seeking. (3) Background checks Except as provided in paragraph (4), the existence of a record of an individual which has been sealed pursuant to this section, or the information contained therein, shall not be included in any background check conducted on such individual. (4) Exceptions (A) Law enforcement and court access An officer or employee of a law enforcement agency or a court may access a record of an individual which has been sealed pursuant to this section and is in the possession of the agency or court, or another law enforcement agency or court, solely\u2014 (i) for investigatory or prosecutorial purposes; or (ii) for a background check that relates to\u2014 (I) employment with a law enforcement agency; (II) any position that a Federal agency designates as a\u2014 (aa) national security position; or (bb) high-risk, public trust position; (III) the manufacture, importation, sale, transfer, possession, or carrying of firearms, explosives, or ammunition; or (IV) employment for a position involving the manufacture, importation, handling, sale, or transfer of controlled substances, as that term is defined under the Controlled Substances Act ( 21 U.S.C. 802 ), or where the employment would provide access to such substances. (B) Disclosure An officer or employee of a law enforcement agency or a court may disclose information contained in a sealed record only in order to carry out the purposes described in subparagraph (A). (d) Individual access Any individual whose record has been sealed pursuant to this section or section 3560A may access the information contained in the individual\u2019s sealed record. (e) Penalty for unauthorized disclosure (1) In general Whoever knowingly accesses or discloses information contained in a record sealed under this section or section 3560A in a manner that is prohibited under this section, shall be fined under this title, imprisoned for not more than 1 year, or both. (2) Rule of construction Nothing in this subsection prevents a covered individual or an individual who was the crime victim (as such term is defined in section 3771(e)) from accessing or disclosing information contained in record sealed under this section or section 3560A. (f) Rule of construction Nothing in this section or section 3560A shall abrogate or constrain the authority of a judge or judicial body to vacate a judgment or sentence. (g) Rulemaking The Attorney General shall, by rule, establish a process to ensure that any record in the possession of a Federal agency required to be sealed under this section is automatically sealed in accordance with this section. (h) Applicability This section shall apply to an arrest that occurred or conviction that was entered before, on, or after the date of enactment of this section. Not later than 2 years after the date of the enactment of this section, the Attorney General shall ensure that any record related to an arrest or conviction that occurred or was entered prior to the automatic sealing of such a record, which record is required to be sealed under this section, is so sealed. (i) Employer immunity from liability An employer who employs or otherwise engages an individual whose criminal records were sealed pursuant to this section shall be immune from liability for any claim arising out of the misconduct of the individual, if the misconduct relates to the portion of the criminal records that were sealed pursuant to this section. (j) Establishment of partnerships The Administrative Office of the United States Courts or the Attorney General shall enter into a contract with or make grants to an organization with expertise in creating digital and technological systems to develop an efficient and effective process for sealing records in accordance with this section and section 3560A. This process shall enable access to sealed records by Federal and non-Federal law enforcement agencies for the purposes set forth in subsection (c)(4)(A) of this section. 3560A. Sealing of certain records upon petition (a) Definitions In this section\u2014 (1) the term covered nonviolent offense means a Federal criminal offense that is not\u2014 (A) murder; (B) voluntary manslaughter; (C) kidnapping; (D) aggravated assault; (E) a forcible sex offense; (F) robbery; (G) arson; (H) extortion; or (I) the use or unlawful possession of\u2014 (i) a firearm, as defined in section 5845(a) of the Internal Revenue Code of 1986; or (ii) explosive materials, as defined in section 841(c); (J) a sex offense (as that term is defined in section 111 of the Sex Offender Registration and Notification Act ( 34 U.S.C. 20911 )); (K) torture, in violation of section 2340A; (L) interstate domestic violence, in violation of section 2261; (M) an offense under chapter 77; or (N) an attempt or conspiracy to commit any of the offenses described in subparagraphs (A) through (M); (2) the term eligible individual means an individual who\u2014 (A) has been convicted of a covered nonviolent offense; (B) has fulfilled each requirement of the sentence for the covered nonviolent offense, including\u2014 (i) completing each term of imprisonment, probation, or supervised release; and (ii) satisfying each condition of imprisonment, probation, or supervised release; (C) has not been convicted of more than 2 felonies that are covered nonviolent offenses, including any such convictions that have been sealed (except that for purposes of this subparagraph, 2 or more felony convictions that are covered nonviolent offenses arising out of the same act, or acts committed at the same time, shall be treated as one felony conviction); (D) has not been convicted of any felony that is not a covered nonviolent offense; and (E) has not been convicted for any offense related to treason, terrorism, access and transmission of sensitive defense information, or other national security related convictions; (3) the term petitioner means an individual who files a sealing petition; (4) the term protected information , with respect to a covered nonviolent offense, means any reference to\u2014 (A) an arrest, conviction, or sentence of an individual for the offense; (B) the institution of criminal proceedings against an individual for the offense; or (C) the result of criminal proceedings described in subparagraph (B); (5) the term sealing hearing means a hearing held under subsection (c)(2); and (6) the term sealing petition means a petition for a sealing order filed under subsection (b). (b) Right To file sealing petition (1) In general On and after the date that is 1 year after the date on which the eligible individual has fulfilled each requirement described in subsection (a)(2)(B), an eligible individual may file a petition for a sealing order with respect to a covered nonviolent offense in a district court of the United States. (2) Notice of opportunity to file petition (A) In general If an individual is convicted of a covered nonviolent offense and will potentially be eligible to file a sealing petition with respect to the offense upon fulfilling each requirement of the sentence for the offense as described in subsection (a)(2)(B), the court in which the individual is convicted shall, in writing, inform the individual, on each date described in subparagraph (B), of\u2014 (i) that potential eligibility; (ii) the necessary procedures for filing the sealing petition; and (iii) the benefits of sealing a record. (B) Dates The dates described in this subparagraph are\u2014 (i) the date on which the individual is convicted; and (ii) the date on which the individual has completed every term of imprisonment, probation, or supervised release relating to the offense. (c) Procedures (1) Notification to prosecutor If an individual files a petition under subsection (b), the district court in which the petition is filed shall provide notice of the petition\u2014 (A) to the office of the United States attorney that prosecuted the petitioner for the offense; and (B) upon the request of the petitioner, to any other individual that the petitioner determines may testify as to the\u2014 (i) conduct of the petitioner since the date of the offense; or (ii) reasons that the sealing order should be entered. (2) Notification to crime victims Upon receipt of a notification under paragraph (1)(A) by an office of the United States attorney, the office shall make reasonable efforts to identify any individual who was a crime victim (as such term is defined in section 3771) of the offense and provide notice of the petition. (3) Hearing (A) In general Not later than 180 days after the date on which an individual files a sealing petition, the district court shall\u2014 (i) except as provided in subparagraph (D), conduct a hearing in accordance with subparagraph (B); and (ii) determine whether to enter a sealing order for the individual in accordance with paragraph (4). (B) Opportunity to testify and offer evidence (i) Petitioner The petitioner may testify or offer evidence at the sealing hearing in support of sealing. (ii) Prosecutor The office of a United States attorney that receives notice under paragraph (1)(A) may send a representative to testify or offer evidence at the sealing hearing in support of or against sealing. (iii) Other individuals At the request of a petitioner, the district court in which the petition is filed shall issue a subpoena requiring an individual who receives notice under paragraph (1)(B) to testify or offer evidence at the sealing hearing as to the issues described in clauses (i) and (ii) of that paragraph. (C) Magistrate judges (i) In general A magistrate judge may preside over a hearing under this paragraph, and submit to a judge of the court proposed findings of fact and recommendations for the disposition, by a judge of the court, of any sealing petition filed under this subsection. (ii) Recommendations Not later than 14 days after being served with a copy, any party may serve and file written objections to the proposed findings and recommendations of the magistrate judge as provided by rules of court. A judge of the court shall make a de novo determination of those portions of the report or specified proposed findings or recommendations to which objection is made. A judge of the court may accept, reject, or modify, in whole or in part, the findings or recommendations made by the magistrate judge. The judge may also receive further evidence or recommit the matter to the magistrate judge with instructions. (D) Waiver of hearing If the petitioner and the United States attorney that receives notice under paragraph (1)(A) so agree, the court shall make a determination under paragraph (4) without a hearing. (4) Basis for decision (A) In general In determining whether to enter a sealing order with respect to protected information relating to a covered nonviolent offense, the court\u2014 (i) shall consider\u2014 (I) the petition and any documents in the possession of the court; and (II) all evidence and testimony presented at the sealing hearing, if such a hearing is conducted; (ii) may not consider any non-Federal crimes for which the petitioner has not been convicted; and (iii) shall balance\u2014 (I) (aa) the interest of public knowledge and safety; and (bb) the legitimate interest, if any, of the Government in maintaining the accessibility of the protected information, including any potential impact of sealing the protected information on Federal licensure, permit, or employment restrictions; against (II) (aa) the conduct and demonstrated desire of the petitioner to be rehabilitated and positively contribute to the community; and (bb) the interest of the petitioner in having the protected information sealed, including the harm of the protected information to the ability of the petitioner to secure and maintain employment. (B) Burden on government The burden shall be on the Government to show that the interests under subclause (I) of subparagraph (A)(iii) outweigh the interests of the petitioner under subclause (II) of that subparagraph. (5) Waiting period after denial If the district court denies a sealing petition, the petitioner may not file a new sealing petition with respect to the same offense until the date that is 2 years after the date of the denial. (6) Universal form The Director of the Administrative Office of the United States Courts shall create a universal form, available over the internet and in paper form, that an individual may use to file a sealing petition. (7) Fee waiver The Director of the Administrative Office of the United States Courts shall by regulation establish a minimally burdensome process under which indigent petitioners may obtain a waiver of any fee for filing a sealing petition. (8) Effect of sealing Subsections (c) through (e) of section 3560 shall apply to any record that is sealed under this section. (9) Public defender eligibility The district court shall appoint counsel in accordance with the plan of the district court in operation under section 3006A to represent a petitioner for purposes of this section. (d) Rule of construction Nothing in this section may be construed to require a covered individual (as such term is defined in section 3560) to submit a sealing petition with respect to records required to be automatically sealed under section 3560. (e) Reporting Not later than 2 years after the date of enactment of this section, and each year thereafter, each district court of the United States shall issue a public report that\u2014 (1) describes\u2014 (A) the number of sealing petitions granted and denied under this section; and (B) the number of instances in which the office of a United States attorney supported or opposed a sealing petition; (2) includes any supporting data that the court determines relevant and that does not name any petitioner; and (3) disaggregates all relevant data by race, ethnicity, gender, and the nature of the offense. (f) Employer immunity from liability An employer who employs or otherwise engages an individual whose criminal records were sealed pursuant to this section shall be immune from liability for any claim arising out of the misconduct of the individual, if the misconduct relates to the portion of the criminal records that were sealed pursuant to this section. .\n##### (b) Table of sections\nThe table of sections for subchapter A of chapter 227 of title 18, United States Code, is amended by inserting after the item relating to section 3559 the following:\n3560. Automatic sealing of certain records. 3560A. Sealing of certain records upon petition. .",
      "versionDate": "2025-04-30",
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
        "actionDate": "2025-05-01",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1580",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Clean Slate Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-21T12:30:17Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3114ih.xml"
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
      "title": "Clean Slate Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clean Slate Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T06:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require automatic sealing of certain criminal records, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T06:33:56Z"
    }
  ]
}
```
